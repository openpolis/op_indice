from django.shortcuts import render_to_response
from charts.models import OppVIndicePolitico

extraction_date = '2010-11-30'

def mps(request, group_by, type):
  if  type=='Deputati':
    tree = 'C'
  else:
    tree = 'S'
    
  records = OppVIndicePolitico.objects.db_manager('opp').raw(OppVIndicePolitico.raw_sqls[group_by], [extraction_date, tree])
  return render_to_response("charts/parlamentari_%s.html" % group_by, { 'object_list': records, 'type': type })
  