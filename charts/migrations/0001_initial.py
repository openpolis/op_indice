# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'TextBlockEnIt'
        db.create_table('charts_textblockenit', (
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=100, primary_key=True)),
            ('txt_en', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('html_en', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('txt_it', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('html_it', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('charts', ['TextBlockEnIt'])


    def backwards(self, orm):
        
        # Deleting model 'TextBlockEnIt'
        db.delete_table('charts_textblockenit')


    models = {
        'charts.oppvindicepolitico': {
            'Meta': {'object_name': 'OppVIndicePolitico', 'db_table': "u'opp_v_indice_politico'", 'managed': 'False'},
            'acronimo': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'assenze': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'circoscrizione': ('django.db.models.fields.CharField', [], {'max_length': '180', 'blank': 'True'}),
            'cognome': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indice': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'indice_pos': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'perc_assenze': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'politico_id': ('django.db.models.fields.IntegerField', [], {}),
            'ramo': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'votazoni': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'charts.oppvlastdate': {
            'Meta': {'object_name': 'OppVLastDate', 'db_table': "u'opp_v_last_date'", 'managed': 'False'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'})
        },
        'charts.opvconstituenciesforlocation': {
            'Meta': {'object_name': 'OpVConstituenciesForLocation', 'db_table': "u'op_v_constituency_for_location'", 'managed': 'False'},
            'collegio': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'provincia': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ramo': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        },
        'charts.textblockenit': {
            'Meta': {'object_name': 'TextBlockEnIt'},
            'html_en': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'html_it': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '100', 'primary_key': 'True'}),
            'txt_en': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'txt_it': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['charts']
