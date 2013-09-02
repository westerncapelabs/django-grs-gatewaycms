# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'VumiGoUser'
        db.create_table(u'usersvumigo_vumigouser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('msisdn', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('sex', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('age', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('community', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'usersvumigo', ['VumiGoUser'])


    def backwards(self, orm):
        # Deleting model 'VumiGoUser'
        db.delete_table(u'usersvumigo_vumigouser')


    models = {
        u'usersvumigo.vumigouser': {
            'Meta': {'object_name': 'VumiGoUser'},
            'age': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'community': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'msisdn': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        }
    }

    complete_apps = ['usersvumigo']