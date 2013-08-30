# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Service'
        db.create_table(u'services_service', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=125)),
            ('content_1', self.gf('django.db.models.fields.CharField')(max_length=125, blank=True)),
            ('content_2', self.gf('django.db.models.fields.CharField')(max_length=125, blank=True)),
            ('content_3', self.gf('django.db.models.fields.CharField')(max_length=125, blank=True)),
        ))
        db.send_create_signal(u'services', ['Service'])


    def backwards(self, orm):
        # Deleting model 'Service'
        db.delete_table(u'services_service')


    models = {
        u'services.service': {
            'Meta': {'object_name': 'Service'},
            'content_1': ('django.db.models.fields.CharField', [], {'max_length': '125', 'blank': 'True'}),
            'content_2': ('django.db.models.fields.CharField', [], {'max_length': '125', 'blank': 'True'}),
            'content_3': ('django.db.models.fields.CharField', [], {'max_length': '125', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '125'})
        }
    }

    complete_apps = ['services']