# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'services_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal(u'services', ['Category'])

        # Adding field 'Service.category'
        db.add_column(u'services_service', 'category',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='category', to=orm['services.Category']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'services_category')

        # Deleting field 'Service.category'
        db.delete_column(u'services_service', 'category_id')


    models = {
        u'services.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'services.service': {
            'Meta': {'object_name': 'Service'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'category'", 'to': u"orm['services.Category']"}),
            'content_1': ('django.db.models.fields.CharField', [], {'max_length': '125', 'blank': 'True'}),
            'content_2': ('django.db.models.fields.CharField', [], {'max_length': '125', 'blank': 'True'}),
            'content_3': ('django.db.models.fields.CharField', [], {'max_length': '125', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '125'}),
            'sms': ('django.db.models.fields.CharField', [], {'max_length': '320'})
        }
    }

    complete_apps = ['services']