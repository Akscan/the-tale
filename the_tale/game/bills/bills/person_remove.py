# coding: utf-8

from textgen.words import Noun

from dext.forms import fields

from game.persons.prototypes import PersonPrototype
from game.persons.storage import persons_storage

from game.bills.relations import BILL_TYPE
from game.bills.forms import BaseUserForm, BaseModeratorForm
from game.bills.bills.base_person_bill import BasePersonBill


class UserForm(BaseUserForm):

    person = fields.ChoiceField(label=u'Персонаж')

    def __init__(self, choosen_person_id, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['person'].choices = PersonPrototype.form_choices(only_weak=True, choosen_person=persons_storage[choosen_person_id])


class ModeratorForm(BaseModeratorForm):
    pass


class PersonRemove(BasePersonBill):

    type = BILL_TYPE.PERSON_REMOVE

    UserForm = UserForm
    ModeratorForm = ModeratorForm

    USER_FORM_TEMPLATE = 'bills/bills/person_remove_user_form.html'
    MODERATOR_FORM_TEMPLATE = 'bills/bills/person_remove_moderator_form.html'
    SHOW_TEMPLATE = 'bills/bills/person_remove_show.html'

    CAPTION = u'Закон об изгнании персонажа'
    DESCRIPTION = u'В случае если персонаж утратил доверие духов-хранителей, его можно изгнать из города. Изгонять можно только наименее влиятельных персонажей.'

    def apply(self):
        self.person.move_out_game()
        self.person.place.sync_persons()
        self.person.save()
