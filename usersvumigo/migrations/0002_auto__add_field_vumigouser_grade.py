# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'VumiGoUser.grade'
        db.add_column(u'usersvumigo_vumigouser', 'grade',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=3),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'VumiGoUser.grade'
        db.delete_column(u'usersvumigo_vumigouser', 'grade')


    models = {
        u'usersvumigo.vumigouser': {
            'Meta': {'object_name': 'VumiGoUser'},
            'age': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'community': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'grade': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'msisdn': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        }
    }

    complete_apps = ['usersvumigo']