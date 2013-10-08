# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AirtimeApplication'
        db.create_table(u'gopher_airtimeapplication', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('ratio', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('per_day', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('amount', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('product_key', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'gopher', ['AirtimeApplication'])

        # Adding model 'SendAirtime'
        db.create_table(u'gopher_sendairtime', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('app_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gopher.AirtimeApplication'])),
            ('msisdn', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('product_key', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('amount', self.gf('django.db.models.fields.IntegerField')()),
            ('sent', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'gopher', ['SendAirtime'])


    def backwards(self, orm):
        # Deleting model 'AirtimeApplication'
        db.delete_table(u'gopher_airtimeapplication')

        # Deleting model 'SendAirtime'
        db.delete_table(u'gopher_sendairtime')


    models = {
        u'gopher.airtimeapplication': {
            'Meta': {'object_name': 'AirtimeApplication'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'amount': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'per_day': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'product_key': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'ratio': ('django.db.models.fields.IntegerField', [], {'blank': 'True'})
        },
        u'gopher.sendairtime': {
            'Meta': {'object_name': 'SendAirtime'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'app_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gopher.AirtimeApplication']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'msisdn': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'product_key': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['gopher']