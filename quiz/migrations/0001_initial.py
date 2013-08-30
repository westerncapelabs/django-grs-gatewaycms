# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Quiz'
        db.create_table(u'quiz_quiz', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=180)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'quiz', ['Quiz'])

        # Adding model 'Question'
        db.create_table(u'quiz_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('quiz_id', self.gf('django.db.models.fields.related.ForeignKey')(related_name='question_quiz_id', to=orm['quiz.Quiz'])),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=180)),
        ))
        db.send_create_signal(u'quiz', ['Question'])

        # Adding model 'Answer'
        db.create_table(u'quiz_answer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question_id', self.gf('django.db.models.fields.related.ForeignKey')(related_name='answer_question_id', to=orm['quiz.Question'])),
            ('answer', self.gf('django.db.models.fields.CharField')(max_length=160)),
        ))
        db.send_create_signal(u'quiz', ['Answer'])

        # Adding model 'Response'
        db.create_table(u'quiz_response', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question_id', self.gf('django.db.models.fields.related.ForeignKey')(related_name='response_question_id', to=orm['quiz.Question'])),
            ('response', self.gf('django.db.models.fields.CharField')(max_length=160)),
        ))
        db.send_create_signal(u'quiz', ['Response'])

        # Adding model 'FinalResponse'
        db.create_table(u'quiz_finalresponse', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('quiz_id', self.gf('django.db.models.fields.related.ForeignKey')(related_name='fr_quiz_id', to=orm['quiz.Quiz'])),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=180)),
            ('sms', self.gf('django.db.models.fields.CharField')(max_length=160)),
            ('for_total', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'quiz', ['FinalResponse'])


    def backwards(self, orm):
        # Deleting model 'Quiz'
        db.delete_table(u'quiz_quiz')

        # Deleting model 'Question'
        db.delete_table(u'quiz_question')

        # Deleting model 'Answer'
        db.delete_table(u'quiz_answer')

        # Deleting model 'Response'
        db.delete_table(u'quiz_response')

        # Deleting model 'FinalResponse'
        db.delete_table(u'quiz_finalresponse')


    models = {
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
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'quiz.answer': {
            'Meta': {'object_name': 'Answer'},
            'answer': ('django.db.models.fields.CharField', [], {'max_length': '160'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question_id': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'answer_question_id'", 'to': u"orm['quiz.Question']"})
        },
        u'quiz.finalresponse': {
            'Meta': {'object_name': 'FinalResponse'},
            'for_total': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quiz_id': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fr_quiz_id'", 'to': u"orm['quiz.Quiz']"}),
            'sms': ('django.db.models.fields.CharField', [], {'max_length': '160'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '180'})
        },
        u'quiz.question': {
            'Meta': {'object_name': 'Question'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '180'}),
            'quiz_id': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'question_quiz_id'", 'to': u"orm['quiz.Quiz']"})
        },
        u'quiz.quiz': {
            'Meta': {'object_name': 'Quiz'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '180'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'quiz.response': {
            'Meta': {'object_name': 'Response'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question_id': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'response_question_id'", 'to': u"orm['quiz.Question']"}),
            'response': ('django.db.models.fields.CharField', [], {'max_length': '160'})
        }
    }

    complete_apps = ['quiz']