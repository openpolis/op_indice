from django.shortcuts import render_to_response
from charts.models import OppVIndicePolitico, OppVLastDate
from django.conf import settings

def mps(request, group_by, type):
  if  type=='Deputati':
    tree = 'C'
  else:
    tree = 'S'
    
  last_date = OppVLastDate.objects.db_manager('opp').raw(OppVLastDate.raw_sql, [tree])[0]
  extraction_date = last_date.last_date
  records = OppVIndicePolitico.objects.db_manager('opp').raw(OppVIndicePolitico.raw_sqls[group_by], [extraction_date, tree])
  return render_to_response("charts/parlamentari_%s.html" % group_by, { 'object_list': records, 'type': type, 'extraction_date': extraction_date, 'openparlamento_url': settings.OPENPARLAMENTO_URL })
  
  