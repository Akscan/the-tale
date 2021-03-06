# coding: utf-8
import mock

from dext.settings import settings

from the_tale.common.utils.testcase import TestCase

from the_tale.accounts.prototypes import AccountPrototype
from the_tale.accounts.logic import get_system_user
from the_tale.accounts.personal_messages.prototypes import MessagePrototype

from the_tale.game.logic import create_test_map

from the_tale.portal import signals as portal_signals
from the_tale.portal.conf import portal_settings


class DayStartedSignalTests(TestCase):

    def setUp(self):
        super(DayStartedSignalTests, self).setUp()

        create_test_map()

        self.account = self.accounts_factory.create_account()


    def test_day_started_signal(self):
        self.assertFalse(portal_settings.SETTINGS_ACCOUNT_OF_THE_DAY_KEY in settings)

        self.assertEqual(MessagePrototype._db_count(), 0)

        with mock.patch('the_tale.accounts.workers.accounts_manager.Worker.cmd_run_account_method') as cmd_run_account_method:
            portal_signals.day_started.send(self.__class__)

        self.assertEqual(cmd_run_account_method.call_count, 1)
        self.assertEqual(cmd_run_account_method.call_args, mock.call(account_id=self.account.id,
                                                                     method_name='prolong_premium',
                                                                     data={'days': portal_settings.PREMIUM_DAYS_FOR_HERO_OF_THE_DAY}))

        self.assertEqual(int(settings[portal_settings.SETTINGS_ACCOUNT_OF_THE_DAY_KEY]), self.account.id)

        self.assertEqual(MessagePrototype._db_count(), 1)
        message = MessagePrototype._db_get_object(0)
        self.assertEqual(message.sender_id, get_system_user().id)
        self.assertEqual(message.recipient_id, self.account.id)

    def test_day_started_signal__only_not_premium(self):
        self.assertEqual(AccountPrototype._db_count(), 1)

        self.account.prolong_premium(days=30)
        self.account.save()

        old_premium_end_at = self.account.premium_end_at

        self.assertEqual(MessagePrototype._db_count(), 0)

        portal_signals.day_started.send(self.__class__)

        self.assertEqual(MessagePrototype._db_count(), 0)

        self.account.reload()
        self.assertEqual(old_premium_end_at, self.account.premium_end_at)
