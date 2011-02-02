from django.shortcuts import render_to_response
from charts.models import OppVIndicePolitico

def deputati(request):
  records = OppVIndicePolitico.objects.db_manager('opp').raw(OppVIndicePolitico.raw_sql, ['2010-11-30', 'C'])
  return render_to_response('charts/deputati.html', { 'object_list': records })

def senatori(request):
  records = OppVIndicePolitico.objects.db_manager('opp').raw(OppVIndicePolitico.raw_sql, ['2010-11-30', 'S'])
  return render_to_response('charts/senatori.html', { 'object_list': records })
  