# coding: utf-8
import datetime

from dext.utils import s11n

from textgen.words import Fake

from common.utils.prototypes import BasePrototype
from common.utils.logic import choose_from_interval

from game.game_info import GENDER_ID_2_STR
from game.helpers import add_power_management
from game.prototypes import TimePrototype

from game.heroes.models import Hero

from game.map.places.storage import places_storage, buildings_storage

from game.balance.enums import RACE
from game.balance import constants as c

from game.persons.models import Person, PERSON_STATE
from game.persons.conf import persons_settings
from game.persons.exceptions import PersonsException
from game.persons.relations import PROFESSION_TO_RACE_MASTERY


MASTERY_VERBOSE = ( (0.0, u'полная непригодность'),
                    (0.1, u'бездарность'),
                    (0.2, u'невежда'),
                    (0.3, u'неуч'),
                    (0.4, u'ученик'),
                    (0.5, u'подмастерье'),
                    (0.6, u'умелец'),
                    (0.7, u'мастер'),
                    (0.8, u'эксперт'),
                    (0.9, u'мэтр'),
                    (1.0, u'гений') )


@add_power_management(persons_settings.POWER_HISTORY_LENGTH, PersonsException)
class PersonPrototype(BasePrototype):
    _model_class = Person
    _readonly = ('id', 'created_at_turn', 'place_id', 'name', 'gender', 'race', 'type', 'state', 'out_game_at')
    _get_by = ('id', )

    @property
    def place(self): return places_storage[self._model.place_id]

    @property
    def normalized_name(self): return (Fake(self._model.name), (GENDER_ID_2_STR[self.gender], u'загл'))

    @property
    def race_verbose(self):
        return RACE._ID_TO_TEXT[self.race]

    @property
    def mastery(self):
        mastery = PROFESSION_TO_RACE_MASTERY[self.type.value][self.race]
        building = buildings_storage.get_by_person_id(self.id)
        if building:
           mastery += c.BUILDING_MASTERY_BONUS * building.integrity
        return min(mastery, 1)

    @property
    def has_building(self): return buildings_storage.get_by_person_id(self.id) is not None

    @property
    def mastery_verbose(self): return choose_from_interval(self.mastery, MASTERY_VERBOSE)

    def move_out_game(self):
        self._model.out_game_at = datetime.datetime.now()
        self._model.state = PERSON_STATE.OUT_GAME

    def remove_from_game(self):
        self._model.state = PERSON_STATE.REMOVED

    def cmd_change_power(self, power):
        from game.workers.environment import workers_environment
        if self.place.modifier:
            power = self.place.modifier.modify_power(power)
        workers_environment.highlevel.cmd_change_person_power(self.id, power)

    @property
    def time_before_unfreeze(self):
        current_time = datetime.datetime.now()
        return max(datetime.timedelta(seconds=0),
                   self._model.created_at + datetime.timedelta(seconds=persons_settings.POWER_STABILITY_WEEKS*7*24*60*60) - current_time)

    @property
    def is_stable(self):
        if self.created_at_turn > TimePrototype.get_current_turn_number() - persons_settings.POWER_STABILITY_WEEKS*7*24*c.TURNS_IN_HOUR:
            return True

        power_percent = float(self.power) / self.place.power if self.place.power > 0.0001 else 0.0

        if power_percent  > persons_settings.POWER_STABILITY_PERCENT:
            return True

        return False

    @property
    def out_game(self): return self._model.state == PERSON_STATE.OUT_GAME

    @property
    def in_game(self):  return self._model.state == PERSON_STATE.IN_GAME

    @property
    def data(self):
        if not hasattr(self, '_data'):
            self._data = s11n.from_json(self._model.data)
        return self._data

    @property
    def friends_number(self): return self._model.friends_number
    def update_friends_number(self):
        current_turn = TimePrototype.get_current_turn_number()
        self._model.friends_number = Hero.objects.filter(pref_friend_id=self.id, active_state_end_at__gte=current_turn).count()

    @property
    def enemies_number(self): return self._model.enemies_number
    def update_enemies_number(self):
        current_turn = TimePrototype.get_current_turn_number()
        self._model.enemies_number = Hero.objects.filter(pref_enemy_id=self.id, active_state_end_at__gte=current_turn).count()

    def save(self):
        from game.persons.storage import persons_storage

        self._model.data = s11n.to_json(self.data)
        self._model.save()

        persons_storage.update_version()


    def remove(self):
        self._model.remove()

    @classmethod
    def create(cls, place, race, tp, name, gender, state=None):
        from game.persons.storage import persons_storage

        instance = Person.objects.create(place=place._model,
                                         state=state if state is not None else PERSON_STATE.IN_GAME,
                                         race=race,
                                         type=tp,
                                         gender=gender,
                                         name=name,
                                         created_at_turn=TimePrototype.get_current_turn_number())

        prototype = cls(model=instance)

        persons_storage.add_item(prototype.id, prototype)
        persons_storage.update_version()

        return prototype


    @classmethod
    def form_choices(cls, only_weak=False, choosen_person=None, predicate=lambda place, person: True):
        choices = []

        for place in places_storage.all():
            persons_choices = filter(lambda person: predicate(place, person), place.persons)
            accepted_persons = persons_choices[place.max_persons_number/2:] if only_weak else persons_choices

            if choosen_person is not None and choosen_person.place.id == place.id:
                if choosen_person.id not in [p.id for p in accepted_persons]:
                    accepted_persons.append(choosen_person)

            accepted_persons = sorted(accepted_persons, key=lambda p: p.name)

            persons = tuple( (person.id, person.name) for person in accepted_persons )

            choices.append( ( place.name, persons ) )

        return sorted(choices, key=lambda choice: choice[0])
