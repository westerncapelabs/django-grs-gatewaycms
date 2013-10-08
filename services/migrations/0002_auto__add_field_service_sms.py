# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Service.sms'
        db.add_column(u'services_service', 'sms',
                      self.gf('django.db.models.fields.CharField')(default='Content Pending', max_length=320),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Service.sms'
        db.delete_column(u'services_service', 'sms')


    models = {
        u'services.service': {
            'Meta': {'object_name': 'Service'},
            'content_1': ('django.db.models.fields.CharField', [], {'max_length': '125', 'blank': 'True'}),
            'content_2': ('django.db.models.fields.CharField', [], {'max_length': '125', 'blank': 'True'}),
            'content_3': ('django.db.models.fields.CharField', [], {'max_length': '125', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '125'}),
            'sms': ('django.db.models.fields.CharField', [], {'max_length': '320'})
        }
    }

    complete_apps = ['services']