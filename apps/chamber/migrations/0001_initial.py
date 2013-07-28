# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Sir'
        db.create_table('chamber_sir', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('bio', self.gf('django.db.models.fields.TextField')(max_length=1000)),
            ('date_birth', self.gf('django.db.models.fields.DateField')()),
            ('contact', self.gf('django.db.models.fields.TextField')(max_length=255)),
        ))
        db.send_create_signal('chamber', ['Sir'])

        # Adding model 'RequestContent'
        db.create_table('chamber_requestcontent', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('method', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('path', self.gf('django.db.models.fields.TextField')(max_length=255)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
            ('status_code', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
        ))
        db.send_create_signal('chamber', ['RequestContent'])


    def backwards(self, orm):
        # Deleting model 'Sir'
        db.delete_table('chamber_sir')

        # Deleting model 'RequestContent'
        db.delete_table('chamber_requestcontent')


    models = {
        'chamber.requestcontent': {
            'Meta': {'object_name': 'RequestContent'},
            'date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'path': ('django.db.models.fields.TextField', [], {'max_length': '255'}),
            'status_code': ('django.db.models.fields.IntegerField', [], {'max_length': '3'})
        },
        'chamber.sir': {
            'Meta': {'object_name': 'Sir'},
            'bio': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'contact': ('django.db.models.fields.TextField', [], {'max_length': '255'}),
            'date_birth': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['chamber']