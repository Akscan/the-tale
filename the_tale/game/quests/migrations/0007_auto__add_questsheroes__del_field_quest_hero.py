# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'QuestsHeroes'
        db.create_table('quests_questsheroes', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hero', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['heroes.Hero'])),
            ('quest', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['quests.Quest'])),
        ))
        db.send_create_signal('quests', ['QuestsHeroes'])

        # Deleting field 'Quest.hero'
        db.delete_column('quests_quest', 'hero_id')

    def backwards(self, orm):
        # Deleting model 'QuestsHeroes'
        db.delete_table('quests_questsheroes')


        # User chose to not deal with backwards NULL issues for 'Quest.hero'
        raise RuntimeError("Cannot reverse this migration. 'Quest.hero' and its values cannot be restored.")
    models = {
        'accounts.account': {
            'Meta': {'object_name': 'Account'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'angels.angel': {
            'Meta': {'object_name': 'Angel'},
            'abilities': ('django.db.models.fields.TextField', [], {'default': "'{}'"}),
            'account': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['accounts.Account']", 'unique': 'True'}),
            'energy': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'}),
            'updated_at_turn': ('django.db.models.fields.BigIntegerField', [], {'default': '0'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'heroes.hero': {
            'Meta': {'object_name': 'Hero'},
            'abilities': ('django.db.models.fields.TextField', [], {'default': "'[]'"}),
            'alive': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'angel': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'heroes'", 'null': 'True', 'blank': 'True', 'to': "orm['angels.Angel']"}),
            'bag': ('django.db.models.fields.TextField', [], {'default': "'{}'"}),
            'destiny_points': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'destiny_points_spend': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'equipment': ('django.db.models.fields.TextField', [], {'default': "'{}'"}),
            'experience': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'gender': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'health': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'messages': ('django.db.models.fields.TextField', [], {'default': "'[]'"}),
            'money': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'next_spending': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'pos_from_x': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'pos_from_y': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'pos_invert_direction': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'pos_percents': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'pos_place': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'+'", 'null': 'True', 'blank': 'True', 'to': "orm['places.Place']"}),
            'pos_road': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'+'", 'null': 'True', 'blank': 'True', 'to': "orm['roads.Road']"}),
            'pos_to_x': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'pos_to_y': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'race': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'stat_artifacts_had': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'stat_loot_had': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'stat_money_earned_from_artifacts': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'stat_money_earned_from_loot': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'stat_money_earned_from_quests': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'stat_money_spend_for_artifacts': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'stat_money_spend_for_heal': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'stat_money_spend_for_impact': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'stat_money_spend_for_sharpening': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'stat_money_spend_for_useless': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'stat_pve_deaths': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'stat_pve_kills': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'stat_quests_done': ('django.db.models.fields.BigIntegerField', [], {'default': '0'})
        },
        'places.place': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Place'},
            'data': ('django.db.models.fields.TextField', [], {'default': '{}'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'size': ('django.db.models.fields.IntegerField', [], {}),
            'subtype': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'terrain': ('django.db.models.fields.CharField', [], {'default': "'.'", 'max_length': '1'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'x': ('django.db.models.fields.BigIntegerField', [], {}),
            'y': ('django.db.models.fields.BigIntegerField', [], {})
        },
        'quests.quest': {
            'Meta': {'object_name': 'Quest'},
            'cmd_number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data': ('django.db.models.fields.TextField', [], {'default': "'{}'"}),
            'env': ('django.db.models.fields.TextField', [], {'default': "'{}'"}),
            'heroes': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['heroes.Hero']", 'through': "orm['quests.QuestsHeroes']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'quests.questchoice': {
            'Meta': {'unique_together': "(('quest', 'choice_point'),)", 'object_name': 'QuestChoice'},
            'choice': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'choice_point': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quest': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'choices'", 'to': "orm['quests.Quest']"})
        },
        'quests.questsheroes': {
            'Meta': {'object_name': 'QuestsHeroes'},
            'hero': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['heroes.Hero']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quest': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['quests.Quest']"})
        },
        'roads.road': {
            'Meta': {'unique_together': "(('point_1', 'point_2'),)", 'object_name': 'Road'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'blank': 'True'}),
            'point_1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['places.Place']"}),
            'point_2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['places.Place']"})
        }
    }

    complete_apps = ['quests']