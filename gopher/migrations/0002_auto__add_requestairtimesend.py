# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RequestAirtimeSend'
        db.create_table(u'gopher_requestairtimesend', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('request_application', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gopher.AirtimeApplication'])),
            ('request_send_airtime', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gopher.SendAirtime'], null=True, blank=True)),
            ('msisdn', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('product_key', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('amount', self.gf('django.db.models.fields.IntegerField')()),
            ('sent', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'gopher', ['RequestAirtimeSend'])


    def backwards(self, orm):
        # Deleting model 'RequestAirtimeSend'
        db.delete_table(u'gopher_requestairtimesend')


    models = {
        u'gopher.airtimeapplication': {
            'Meta': {'object_name': 'AirtimeApplication'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'amount': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_per_day': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'product_key': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'ratio': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'gopher.requestairtimesend': {
            'Meta': {'object_name': 'RequestAirtimeSend'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'msisdn': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'product_key': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'request_application': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gopher.AirtimeApplication']"}),
            'request_send_airtime': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gopher.SendAirtime']", 'null': 'True', 'blank': 'True'}),
            'sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
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