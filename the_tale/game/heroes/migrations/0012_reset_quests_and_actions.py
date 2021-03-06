# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-17 18:40
from __future__ import unicode_literals

import json

from django.db import migrations


def reset_actions_and_quests(apps, schema_editor):
    for hero in apps.get_model("heroes", "Hero").objects.all():

        actions = json.loads(hero.actions)

        actions['actions'] = [actions['actions'][0]]

        hero.actions = json.dumps(actions, ensure_ascii=False)

        hero.save()


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0011_make_id_equal_to_account_id'),
    ]

    operations = [
        migrations.RunPython(reset_actions_and_quests)
    ]
