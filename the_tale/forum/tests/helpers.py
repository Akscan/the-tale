# coding: utf-8
from the_tale.common.utils.testcase import TestAccountsFactory

from the_tale.accounts.clans.prototypes import ClanPrototype
from the_tale.accounts.clans.conf import clans_settings


from the_tale.forum.prototypes import (ThreadPrototype,
                              PostPrototype,
                              SubCategoryPrototype,
                              CategoryPrototype)

class ForumFixture(object):

    def __init__(self, accounts_factory):
        self.account_1 = accounts_factory.create_account()
        self.account_2 = accounts_factory.create_account()

        # cat1
        # |-subcat1
        # | |-thread1
        # | | |-post1
        # | |-thread2
        # |-subcat2
        # cat2
        # | subcat3
        # | |- thread3
        # cat3

        self.cat_1 = CategoryPrototype.create(caption='cat1-caption', slug='cat1-slug', order=0)
        # to test, that subcat.id not correlate with order
        self.subcat_2 = SubCategoryPrototype.create(category=self.cat_1, caption='subcat2-caption', order=1, closed=True)
        self.subcat_1 = SubCategoryPrototype.create(category=self.cat_1, caption='subcat1-caption', order=0)
        self.cat_2 = CategoryPrototype.create(caption='cat2-caption', slug='cat2-slug', order=0)
        self.subcat_3 = SubCategoryPrototype.create(category=self.cat_2, caption='subcat3-caption', order=0)
        self.cat_3 = CategoryPrototype.create(caption='cat3-caption', slug='cat3-slug', order=0)

        self.thread_1 = ThreadPrototype.create(self.subcat_1, 'thread1-caption', self.account_1, 'thread1-text')
        self.thread_2 = ThreadPrototype.create(self.subcat_1, 'thread2-caption', self.account_1, 'thread2-text')
        self.thread_3 = ThreadPrototype.create(self.subcat_3, 'thread3-caption', self.account_1, 'thread3-text')

        self.post_1 = PostPrototype.create(self.thread_1, self.account_1, 'post1-text')

        # create test clan and clean it's forum artifacts
        self.clan_category = CategoryPrototype.create(caption='category-1', slug=clans_settings.FORUM_CATEGORY_SLUG, order=0)
        self.clan_1 = ClanPrototype.create(self.account_1, abbr=u'abbr1', name=u'name1', motto=u'motto', description=u'description')
