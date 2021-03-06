# coding: utf-8
import mock
import random

from the_tale.common.utils import testcase

from the_tale.game.logic_storage import LogicStorage
from the_tale.game.logic import create_test_map

from the_tale.game.cards import effects

from the_tale.game.postponed_tasks import ComplexChangeTask

from the_tale.game.cards.tests.helpers import CardsTestMixin

from the_tale.game.companions import storage as companions_storage
from the_tale.game.companions import logic as companions_logic

from the_tale.game.heroes.relations import ITEMS_OF_EXPENDITURE


class ChangeHeroSpendingsCommonTests(testcase.TestCase):
    CARD = None

    def setUp(self):
        super(ChangeHeroSpendingsCommonTests, self).setUp()

    def test_no_new_spendigns(self):
        items = []

        for card in effects.EFFECTS.values():
            if hasattr(card, 'ITEM'):
                items.append(card.ITEM)

        items.append(ITEMS_OF_EXPENDITURE.USELESS)
        items.append(ITEMS_OF_EXPENDITURE.IMPACT)

        self.assertEqual(len(items), len(ITEMS_OF_EXPENDITURE.records))
        self.assertEqual(set(items), set(ITEMS_OF_EXPENDITURE.records))


class ChangeHeroSpendingsMixin(CardsTestMixin):
    CARD = None

    def setUp(self):
        super(ChangeHeroSpendingsMixin, self).setUp()

        create_test_map()

        self.account_1 = self.accounts_factory.create_account()

        self.storage = LogicStorage()
        self.storage.load_account_data(self.account_1)

        self.hero = self.storage.accounts_to_heroes[self.account_1.id]

        self.card = self.CARD()

        old_companion_record = random.choice(companions_storage.companions.all())
        self.hero.set_companion(companions_logic.create_companion(old_companion_record))


    def test_use(self):

        # sure that quests will be loaded and not cal mark_updated
        self.hero.quests.mark_updated()

        for item in ITEMS_OF_EXPENDITURE.records:
            if item == self.CARD.ITEM:
                continue

            self.hero.next_spending = item

            with mock.patch('the_tale.game.quests.container.QuestsContainer.mark_updated') as mark_updated:
                result, step, postsave_actions = self.card.use(**self.use_attributes(storage=self.storage, hero=self.hero))

            self.assertEqual(mark_updated.call_count, 1)

            self.assertEqual(self.hero.next_spending, self.CARD.ITEM)

            self.assertEqual((result, step, postsave_actions), (ComplexChangeTask.RESULT.SUCCESSED, ComplexChangeTask.STEP.SUCCESS, ()))


    def test_equal(self):
        self.hero.next_spending = self.CARD.ITEM

        with mock.patch('the_tale.game.quests.container.QuestsContainer.mark_updated') as mark_updated:
            result, step, postsave_actions = self.card.use(**self.use_attributes(storage=self.storage, hero=self.hero))

        self.assertEqual(mark_updated.call_count, 0)

        self.assertEqual((result, step, postsave_actions), (ComplexChangeTask.RESULT.FAILED, ComplexChangeTask.STEP.ERROR, ()))



class ChangeHeroSpendingsToInstantHealTests(ChangeHeroSpendingsMixin, testcase.TestCase):
    CARD = effects.ChangeHeroSpendingsToInstantHeal

class ChangeHeroSpendingsToBuyingArtifactTests(ChangeHeroSpendingsMixin, testcase.TestCase):
    CARD = effects.ChangeHeroSpendingsToBuyingArtifact

class ChangeHeroSpendingsToSharpeingArtifactTests(ChangeHeroSpendingsMixin, testcase.TestCase):
    CARD = effects.ChangeHeroSpendingsToSharpeingArtifact

class ChangeHeroSpendingsToRepairingArtifactTests(ChangeHeroSpendingsMixin, testcase.TestCase):
    CARD = effects.ChangeHeroSpendingsToRepairingArtifact

class ChangeHeroSpendingsToExperienceTests(ChangeHeroSpendingsMixin, testcase.TestCase):
    CARD = effects.ChangeHeroSpendingsToExperience

class ChangeHeroSpendingsToHealCompanionTests(ChangeHeroSpendingsMixin, testcase.TestCase):
    CARD = effects.ChangeHeroSpendingsToHealCompanion

    def test_use__no_companion(self):
        self.hero.remove_companion()

        for item in ITEMS_OF_EXPENDITURE.records:
            if item == self.CARD.ITEM:
                continue

            self.hero.next_spending = item

            with mock.patch('the_tale.game.quests.container.QuestsContainer.mark_updated') as mark_updated:
                result, step, postsave_actions = self.card.use(**self.use_attributes(storage=self.storage, hero=self.hero))

            self.assertEqual(mark_updated.call_count, 0)

            self.assertEqual((result, step, postsave_actions), (ComplexChangeTask.RESULT.FAILED, ComplexChangeTask.STEP.ERROR, ()))

            self.assertEqual(self.hero.next_spending, item)
