from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.sites.models import Site
from django.http import Http404
from charts.models import OppVIndicePolitico, OppVLastDate, OpVConstituenciesForLocation

def home(request, extraction_date, openparlamento_url, fetch_s3_images):
  return render_to_response("charts/home.html", 
    {
      'openparlamento_url': openparlamento_url,
      'extraction_date': extraction_date,
      'fetch_s3_images': fetch_s3_images,
      'current_site_domain': Site.objects.get_current().domain,
      'block_name': "home.%s" %  request.LANGUAGE_CODE
    },
    context_instance=RequestContext(request)
  )
  
def about(request):
  return render_to_response("charts/about.html", 
    {
      'block_name': "about.%s" %  request.LANGUAGE_CODE
    },
    context_instance=RequestContext(request)
  )
    

def mps(request, group_by, type, extraction_date, openparlamento_url):
  if  type=='deputati':
    tree = 'C'
  else:
    tree = 'S'
    
  records = OppVIndicePolitico.objects.db_manager('opp').raw(OppVIndicePolitico.raw_sqls[group_by], [extraction_date, tree])
  return render_to_response("charts/parlamentari_%s.html" % group_by, 
    { 
      'object_list': records, 
      'objects_count': sum(1 for rec in records), 
      'type': type, 
      'extraction_date': extraction_date, 
      'openparlamento_url': openparlamento_url,
    },
    context_instance=RequestContext(request)
  )
  
def location(request, op_location_name, extraction_date, openparlamento_url, fetch_s3_images):
  constituencies = OpVConstituenciesForLocation.objects.db_manager('op').raw(OpVConstituenciesForLocation.raw_sql, [op_location_name])
  c_hash = {}
  for c in constituencies:
      c_hash[c.ramo] = c.collegio

  if len(c_hash) == 0:
    raise Http404

      
  return render_to_response("charts/location.html", 
    {
      'constituencies' : c_hash,
      'op_location_name': op_location_name, 
      'extraction_date': extraction_date, 
      'openparlamento_url': openparlamento_url,
      'fetch_s3_images': fetch_s3_images 
    },
    context_instance=RequestContext(request)
  )
  
  