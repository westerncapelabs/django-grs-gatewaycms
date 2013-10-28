# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'AirtimeApplication.sms'
        db.add_column(u'gopher_airtimeapplication', 'sms',
                      self.gf('django.db.models.fields.CharField')(max_length=160, null=True, blank=True),
                      keep_default=False)

        # Adding field 'AirtimeApplication.created_at'
        db.add_column(u'gopher_airtimeapplication', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 10, 28, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'AirtimeApplication.sms'
        db.delete_column(u'gopher_airtimeapplication', 'sms')

        # Deleting field 'AirtimeApplication.created_at'
        db.delete_column(u'gopher_airtimeapplication', 'created_at')


    models = {
        u'gopher.airtimeapplication': {
            'Meta': {'object_name': 'AirtimeApplication'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'amount': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_per_day': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'product_key': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'ratio': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sms': ('django.db.models.fields.CharField', [], {'max_length': '160', 'null': 'True', 'blank': 'True'})
        },
        u'gopher.requestairtimesend': {
            'Meta': {'object_name': 'RequestAirtimeSend'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'msisdn': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'product_key': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'request_application': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'request_application'", 'to': u"orm['gopher.AirtimeApplication']"}),
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