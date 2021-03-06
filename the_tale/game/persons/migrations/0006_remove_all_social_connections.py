# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-19 16:51
from __future__ import unicode_literals

from django.db import migrations


def remove_all_social_connections(apps, schema_editor):
    apps.get_model("persons", "SocialConnection").objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0005_remove_removed_persons'),
    ]

    operations = [
        migrations.RunPython(remove_all_social_connections)
    ]
