# coding: utf-8

from the_tale.finances.shop import goods
from the_tale.finances.shop import exceptions
from the_tale.finances.shop import relations
from the_tale.finances.shop.conf import payments_settings

PREMIUM_DAYS_DESCRIPTION = u'''
<p>
Подписка даёт следующие преимущества:
</p>

<ul>
  <li>герой оказывает влияние на мир;</li>
  <li>можно голосовать;</li>
  <li>можно ремонтировать здания;</li>
  <li>получаемые карты судьбы можно продавать на рынке;</li>
  <li>на 50% увеличивается получаемый героем опыт;</li>
  <li>на 50% увеличивается скорость изменения черт;</li>
  <li>на 200% увеличивается максимум энергии (до 72 единиц);</li>
  <li>жизнь героя не замедляется при длительном отсутствии игрока в игре.</li>
</ul>
'''

PREFERENCES_DESCRIPTION = u'''
<p>
У каждого героя есть предпочтения, в соответствии с которыми он строит своё поведение.<br/>
Они доступны не сразу, а открываются с ростом уровня.<br/>
Вы можете не ждать и получить доступ к любому из них за небольшое количество печенек.
</p>
'''

GUILDS_DESCRIPTION = u'''
<p>
Гильдии — это объединения игроков, преследующих одну и ту же цель и желающих согласовывать свои действия в Пандоре.<br/>
Создать гильдию может любой игрок, если у него достаточно могущества.<br/>
Если Ваше могущество меньше, Вы можете купить разрешение на владение гильдией.
</p>
'''

RANDOM_PREMIUM_CHEST_DESCRIPTION = u'''
<p>
Подарите подписку на %(days)s дней случайному активному игроку (не подписчику) и получите один из подарков:
</p>
<ul>
%(gifts)s
</ul>
<p>
Подарки указаны от самого вероятного к самому редкому.
</p>

<p>
Чем больше подписчиков, тем увлекательнее жизнь Пандоры!
</p>
''' % {'gifts': '\n'.join(u'<li>%s</li>' % reward.description
                          for reward in sorted(relations.RANDOM_PREMIUM_CHEST_REWARD.records, key=lambda r: -r.priority)),
       'days': payments_settings.RANDOM_PREMIUM_DAYS }

def permanent_purchase(uid, purchase_type, cost, transaction_description):
    return goods.PermanentPurchase(uid=uid,
                                   name=purchase_type.text,
                                   full_name=purchase_type.full_name,
                                   description=purchase_type.description,
                                   cost=cost,
                                   purchase_type=purchase_type,
                                   transaction_description=transaction_description)

def permanent_permission_purchase(uid, purchase_type, cost):
    return permanent_purchase(uid=uid,
                              purchase_type=purchase_type,
                              cost=cost,
                              transaction_description=u'Снятие ограничения уровня на предпочтение героя «%s»' % purchase_type.preference_type.text)


RANDOM_PREMIUM_CHEST = goods.PurchaseGroup(type=relations.GOODS_GROUP.CHEST,
                                           name=u'Делай добро и дари подписку!',
                                           short_name=u'Сделать добро',
                                           description=RANDOM_PREMIUM_CHEST_DESCRIPTION,
                                           items=[ goods.RandomPremiumChest(uid='random-premium-chest',
                                                                            cost=200,
                                                                            description=RANDOM_PREMIUM_CHEST_DESCRIPTION,
                                                                            name=u'Сделать добро',
                                                                            full_name=u'Делай добро и дари подписку!',
                                                                            transaction_description=u'Подписка в подарок случайному игроку') ])


PRICE_GROUPS = [RANDOM_PREMIUM_CHEST,

                goods.PurchaseGroup(type=relations.GOODS_GROUP.PREMIUM,
                                    name=u'Подписка',
                                    description=PREMIUM_DAYS_DESCRIPTION,
                                    items=[ goods.PremiumDays(uid=u'subscription-15',
                                                              name=u'15 дней',
                                                              full_name=u'15 дней подписки',
                                                              description=PREMIUM_DAYS_DESCRIPTION,
                                                              cost=180,
                                                              days=15,
                                                              transaction_description=u'Продление подписки на 15 дней.'),

                                            goods.PremiumDays(uid=u'subscription-30',
                                                              name=u'30 дней',
                                                              full_name=u'30 дней подписки',
                                                              description=PREMIUM_DAYS_DESCRIPTION,
                                                              cost=300,
                                                              days=30,
                                                              transaction_description=u'Продление подписки на 30 дней.'),

                                            goods.PremiumDays(uid=u'subscription-90',
                                                              name=u'90 дней',
                                                              full_name=u'90 дней подписки',
                                                              description=PREMIUM_DAYS_DESCRIPTION,
                                                              cost=750,
                                                              days=90,
                                                              transaction_description=u'Продление подписки на 90 дней.'),

                                            permanent_purchase(uid=u'subscription-infinit',
                                                               purchase_type=relations.PERMANENT_PURCHASE_TYPE.INFINIT_SUBSCRIPTION,
                                                               cost=6000,
                                                               transaction_description=u'Приобретение вечной подписки.')  ]),

                goods.PurchaseGroup(type=relations.GOODS_GROUP.PREFERENCES,
                                    name=u'Предпочтения',
                                    description=PREFERENCES_DESCRIPTION,
                                    items=[ permanent_permission_purchase(uid=u'preference-companion-dedication',
                                                                          cost=10,
                                                                          purchase_type=relations.PERMANENT_PURCHASE_TYPE.PREFERENCE_COMPANION_DEDICATION),

                                            permanent_permission_purchase(uid=u'preference-place',
                                                                          cost=20,
                                                                          purchase_type=relations.PERMANENT_PURCHASE_TYPE.PREFERENCE_PLACE),

                                            permanent_permission_purchase(uid=u'preference-mob',
                                                                          cost=30,
                                                                          purchase_type=relations.PERMANENT_PURCHASE_TYPE.PREFERENCE_MOB),

                                            permanent_permission_purchase(uid=u'preference-friend',
                                                                          cost=40,
                                                                          purchase_type=relations.PERMANENT_PURCHASE_TYPE.PREFERENCE_FRIEND),

                                            permanent_permission_purchase(uid=u'preference-archetype',
                                                                          cost=50,
                                                                          purchase_type=relations.PERMANENT_PURCHASE_TYPE.PREFERENCE_ARCHETYPE),

                                            permanent_permission_purchase(uid=u'preference-enemy',
                                                                          cost=60,
                                                                          purchase_type=relations.PERMANENT_PURCHASE_TYPE.PREFERENCE_ENEMY),

                                            permanent_permission_purchase(uid=u'preference-companion-empathy',
                                                                          cost=70,
                                                                          purchase_type=relations.PERMANENT_PURCHASE_TYPE.PREFERENCE_COMPANION_EMPATHY),

                                            permanent_permission_purchase(uid=u'preference-favorite-item',
                                                                          cost=80,
                                                                          purchase_type=relations.PERMANENT_PURCHASE_TYPE.PREFERENCE_FAVORITE_ITEM),

                                            permanent_permission_purchase(uid=u'preference-risk-level',
                                                                          cost=90,
                                                                          purchase_type=relations.PERMANENT_PURCHASE_TYPE.PREFERENCE_RISK_LEVEL),

                                            permanent_permission_purchase(uid=u'preference-equipment-slot',
                                                                          cost=100,
                                                                          purchase_type=relations.PERMANENT_PURCHASE_TYPE.PREFERENCE_EQUIPMENT_SLOT)
                                                                           ]),

                goods.PurchaseGroup(type=relations.GOODS_GROUP.CLANS,
                                    name=u'Гильдии',
                                    description=GUILDS_DESCRIPTION,
                                    items=[ permanent_purchase(uid=u'clan-ownership-right',
                                                               cost=150,
                                                               purchase_type=relations.PERMANENT_PURCHASE_TYPE.CLAN_OWNERSHIP_RIGHT,
                                                               transaction_description=u'Приобретение разрешения на владение гильдией.') ]),
                ]



PURCHASES_BY_UID = {}

for group in PRICE_GROUPS:
    for purchase in group.items:
        if purchase.uid in PURCHASES_BY_UID:
            raise exceptions.DuplicateUIDsInPriceListError('duplicate uids in price list')
        PURCHASES_BY_UID[purchase.uid] = purchase
