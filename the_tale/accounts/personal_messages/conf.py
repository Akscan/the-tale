# coding: utf-8

import datetime

from dext.utils.app_settings import app_settings


personal_messages_settings = app_settings('PERSONAL_MESSAGES',
                                          MESSAGES_ON_PAGE=10,
                                          SYSTEM_MESSAGES_LEAVE_TIME=datetime.timedelta(seconds=2*7*24*60*60))
