# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'MetaAction.bundle'
        db.alter_column(u'actions_metaaction', 'bundle_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['game.Bundle'], null=True, on_delete=models.PROTECT))

        # Changing field 'MetaActionMember.action'
        db.alter_column(u'actions_metaactionmember', 'action_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.PROTECT, to=orm['actions.MetaAction']))

        # Changing field 'MetaActionMember.hero'
        db.alter_column(u'actions_metaactionmember', 'hero_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.PROTECT, to=orm['heroes.Hero']))

    def backwards(self, orm):

        # Changing field 'MetaAction.bundle'
        db.alter_column(u'actions_metaaction', 'bundle_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['game.Bundle'], null=True))

        # Changing field 'MetaActionMember.action'
        db.alter_column(u'actions_metaactionmember', 'action_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['actions.MetaAction']))

        # Changing field 'MetaActionMember.hero'
        db.alter_column(u'actions_metaactionmember', 'hero_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['heroes.Hero']))

    models = {
        u'accounts.account': {
            'Meta': {'ordering': "['nick']", 'object_name': 'Account'},
            'active_end_at': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'ban_forum_end_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(1970, 1, 1, 0, 0)', 'db_index': 'True'}),
            'ban_game_end_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(1970, 1, 1, 0, 0)', 'db_index': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(1970, 1, 1, 0, 0)', 'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_fast': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_news_remind_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(1970, 1, 1, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            'new_messages_number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'nick': ('django.db.models.fields.CharField', [], {'default': "u''", 'unique': 'True', 'max_length': '128', 'db_index': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'personal_messages_subscription': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'premium_end_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(1970, 1, 1, 0, 0)', 'db_index': 'True'}),
            'premium_expired_notification_send_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(1970, 1, 1, 0, 0)', 'db_index': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '4096', 'null': 'True'}),
            'referer_domain': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '256', 'null': 'True', 'db_index': 'True'}),
            'referral_of': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['accounts.Account']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'referrals_number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(1970, 1, 1, 0, 0)', 'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'actions.metaaction': {
            'Meta': {'object_name': 'MetaAction'},
            'bundle': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['game.Bundle']", 'null': 'True', 'on_delete': 'models.PROTECT'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data': ('django.db.models.fields.TextField', [], {'default': "'{}'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'percents': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'state': ('django.db.models.fields.CharField', [], {'default': "'uninitialized'", 'max_length': '50'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'actions.metaactionmember': {
            'Meta': {'object_name': 'MetaActionMember'},
            'action': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'on_delete': 'models.PROTECT', 'to': u"orm['actions.MetaAction']"}),
            'context': ('django.db.models.fields.TextField', [], {'default': "'{}'"}),
            'hero': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'on_delete': 'models.PROTECT', 'to': u"orm['heroes.Hero']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'game.bundle': {
            'Meta': {'object_name': 'Bundle'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2000, 1, 1, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True'}),
            'type': ('django.db.models.fields.IntegerField', [], {})
        },
        u'heroes.hero': {
            'Meta': {'object_name': 'Hero'},
            'abilities': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'account': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'heroes'", 'null': 'True', 'blank': 'True', 'to': u"orm['accounts.Account']"}),
            'actions': ('django.db.models.fields.TextField', [], {'default': "'{}'"}),
            'active_state_end_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(1970, 1, 1, 0, 0)', 'db_index': 'True'}),
            'bag': ('django.db.models.fields.TextField', [], {'default': "'{}'"}),
            'ban_state_end_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(1970, 1, 1, 0, 0)', 'db_index': 'True'}),
            'created_at_turn': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'diary': ('django.db.models.fields.TextField', [], {'default': "'[]'"}),
            'energy': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'equipment': ('django.db.models.fields.TextField', [], {'default': "'{}'"}),
            'experience': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'gender': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'health': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_alive': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_fast': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'last_energy_regeneration_at_turn': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'level': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'messages': ('django.db.models.fields.TextField', [], {'default': "'[]'"}),
            'might': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'might_updated_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2000, 1, 1, 0, 0)', 'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'money': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'name_forms': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'next_spending': ('rels.django_staff.TableIntegerField', [], {}),
            'places_history': ('django.db.models.fields.TextField', [], {'default': "'{}'"}),
            'pos_from_x': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'pos_from_y': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'pos_invert_direction': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'pos_percents': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'pos_place': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'on_delete': 'models.PROTECT', 'default': 'None', 'to': u"orm['places.Place']", 'blank': 'True', 'null': 'True'}),
            'pos_road': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'on_delete': 'models.PROTECT', 'default': 'None', 'to': u"orm['roads.Road']", 'blank': 'True', 'null': 'True'}),
            'pos_to_x': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'pos_to_y': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'pref_enemy': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'on_delete': 'models.PROTECT', 'default': 'None', 'to': u"orm['persons.Person']", 'blank': 'True', 'null': 'True'}),
            'pref_enemy_changed_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2000, 1, 1, 0, 0)'}),
            'pref_energy_regeneration_type': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'pref_energy_regeneration_type_changed_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2000, 1, 1, 0, 0)'}),
            'pref_equipment_slot': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'pref_equipment_slot_changed_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2000, 1, 1, 0, 0)'}),
            'pref_friend': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'on_delete': 'models.PROTECT', 'default': 'None', 'to': u"orm['persons.Person']", 'blank': 'True', 'null': 'True'}),
            'pref_friend_changed_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2000, 1, 1, 0, 0)'}),
            'pref_mob': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['mobs.MobRecord']", 'null': 'True', 'on_delete': 'models.PROTECT', 'blank': 'True'}),
            'pref_mob_changed_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2000, 1, 1, 0, 0)'}),
            'pref_place': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'on_delete': 'models.PROTECT', 'default': 'None', 'to': u"orm['places.Place']", 'blank': 'True', 'null': 'True'}),
            'pref_place_changed_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2000, 1, 1, 0, 0)'}),
            'premium_state_end_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(1970, 1, 1, 0, 0)', 'db_index': 'True'}),
            'pvp': ('django.db.models.fields.TextField', [], {'default': "'{}'"}),
            'quests_history': ('django.db.models.fields.TextField', [], {'default': "'{}'"}),
            'race': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'raw_power': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'saved_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(1970, 1, 1, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'saved_at_turn': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'stat_artifacts_had': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'stat_loot_had': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'stat_money_earned_from_artifacts': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'stat_money_earned_from_help': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'stat_money_earned_from_loot': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'stat_money_earned_from_quests': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'stat_money_spend_for_artifacts': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'stat_money_spend_for_experience': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'stat_money_spend_for_heal': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'stat_money_spend_for_impact': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'stat_money_spend_for_sharpening': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'stat_money_spend_for_useless': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'stat_pve_deaths': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'stat_pve_kills': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'stat_pvp_battles_1x1_draws': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'stat_pvp_battles_1x1_number': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'stat_pvp_battles_1x1_victories': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'stat_quests_done': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'ui_caching_started_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2000, 1, 1, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'})
        },
        u'mobs.mobrecord': {
            'Meta': {'object_name': 'MobRecord'},
            'abilities': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "u''"}),
            'editor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['accounts.Account']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32', 'db_index': 'True'}),
            'name_forms': ('django.db.models.fields.TextField', [], {}),
            'state': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'terrains': ('django.db.models.fields.TextField', [], {}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'})
        },
        u'persons.person': {
            'Meta': {'object_name': 'Person'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2000, 1, 1, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            'created_at_turn': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'data': ('django.db.models.fields.TextField', [], {'default': "u'{}'"}),
            'enemies_number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'friends_number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'gender': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'out_game_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2000, 1, 1, 0, 0)'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'persons'", 'on_delete': 'models.PROTECT', 'to': u"orm['places.Place']"}),
            'race': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'state': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'type': ('rels.django_staff.TableIntegerField', [], {})
        },
        u'places.place': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Place'},
            'data': ('django.db.models.fields.TextField', [], {'default': "u'{}'"}),
            'description': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'expected_size': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'freedom': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'goods': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'heroes_number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modifier': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150', 'db_index': 'True'}),
            'name_forms': ('django.db.models.fields.TextField', [], {'default': "u''"}),
            'production': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'race': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'safety': ('django.db.models.fields.FloatField', [], {'default': '0.75'}),
            'size': ('django.db.models.fields.IntegerField', [], {}),
            'transport': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_at_turn': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'x': ('django.db.models.fields.BigIntegerField', [], {}),
            'y': ('django.db.models.fields.BigIntegerField', [], {})
        },
        u'roads.road': {
            'Meta': {'unique_together': "(('point_1', 'point_2'),)", 'object_name': 'Road'},
            'exists': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'blank': 'True'}),
            'path': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'point_1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['places.Place']"}),
            'point_2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['places.Place']"})
        }
    }

    complete_apps = ['actions']