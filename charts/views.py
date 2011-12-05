from datetime import datetime

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.sites.models import Site
from django.http import Http404

from json_proxy import get_json_data

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
  
def info(request):
  return render_to_response("charts/info.html", 
    {
      'block_name': "info.%s" %  request.LANGUAGE_CODE
    },
    context_instance=RequestContext(request)
  )
    

def mps(request, group_by, type, extraction_date, openparlamento_url):
  if group_by == 'constituency':
    json_endpoint = "json_getIndexChartsRegions"
  elif group_by == 'group':
    json_endpoint = "json_getIndexChartsGroups"
  elif group_by == 'sex':
    json_endpoint = "json_getIndexChartsSex"
  else :
    json_endpoint = "json_getIndexChartsPoliticians"

  if  type=='deputati':
    tree = 'C'
  else:
    tree = 'S'
    
  last_date = datetime.strftime(extraction_date, "%Y-%m-%d")
  json_url = "%s/%s?ramo=%s&data=%s" % (openparlamento_url, json_endpoint, tree, last_date)
  
  import sys
  print >> sys.stderr, "json url: %s" % json_url
  
  records = get_json_data(json_url)
  
  return render_to_response("charts/parlamentari_%s.html" % group_by, 
    { 
      'object_list': records, 
      'objects_count': len(records), 
      'type': type, 
      'extraction_date': extraction_date, 
      'openparlamento_url': openparlamento_url,
    },
    context_instance=RequestContext(request)
  )
  
def location(request, op_constituency_name, extraction_date, openparlamento_url, fetch_s3_images):
  c_hash = {}
  c_hash['camera'] = op_constituency_name
  c_hash['senato'] = op_constituency_name
  
  if (op_constituency_name[-1:] == '1' or
     op_constituency_name[-1:] == '2' or
     op_constituency_name[-1:] == '3') :
     c_hash['senato'] = op_constituency_name[:-2]
    
  if len(c_hash) == 0:
    raise Http404

      
  return render_to_response("charts/location.html", 
    {
      'constituencies' : c_hash,
      'extraction_date': extraction_date, 
      'openparlamento_url': openparlamento_url,
      'fetch_s3_images': fetch_s3_images 
    },
    context_instance=RequestContext(request)
  )
  
  
