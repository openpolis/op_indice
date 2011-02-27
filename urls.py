from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.conf import settings
from django.utils import translation
from datetime import datetime
from json_proxy import get_json_data

last_date_data = get_json_data("http://%s/json_getLastDateForPoliticianHistoryCache" % settings.OPENPARLAMENTO_URL)
extraction_date = datetime.strptime(last_date_data['last_date'], '%Y-%m-%d')

from django.contrib import admin
admin.autodiscover()

# extract last date for politician_history cached data from opp
# TODO: move to a proper location (proxy json request handler)

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),

    # home page
    (r'^$', 'charts.views.home', { 
      'openparlamento_url': settings.OPENPARLAMENTO_URL, 
      'extraction_date': extraction_date,
      'fetch_s3_images': settings.FETCH_S3_IMAGES }),  
    
    # info page
    (r'^info.html$', 'charts.views.info'),  

    # complete charts
    (r'^deputati.html$', 'charts.views.mps', 
      { 'type': 'deputati', 'group_by': 'list',
        'openparlamento_url': settings.OPENPARLAMENTO_URL, 'extraction_date': extraction_date }),
    (r'^deputati/(?P<group_by>\w+).html$', 'charts.views.mps', 
      { 'type': 'deputati', 
        'openparlamento_url': settings.OPENPARLAMENTO_URL, 'extraction_date': extraction_date }),    
    (r'^senatori.html$', 'charts.views.mps', { 
        'type': 'senatori', 'group_by': 'list',
        'openparlamento_url': settings.OPENPARLAMENTO_URL, 'extraction_date': extraction_date }),
    (r'^senatori/(?P<group_by>\w+).html$', 'charts.views.mps', { 
        'type': 'senatori',
        'openparlamento_url': settings.OPENPARLAMENTO_URL, 'extraction_date': extraction_date }),    
    (r'^i18n/', include('django.conf.urls.i18n')),
    (r'^(?P<op_constituency_name>[\w-]+).html$', 
      'charts.views.location', { 'openparlamento_url': settings.OPENPARLAMENTO_URL, 
                                 'extraction_date': extraction_date,
                                 'fetch_s3_images': settings.FETCH_S3_IMAGES }),    
)

# static media (not for production!)
if (settings.ENVIRONMENT != 'production'):
  urlpatterns += patterns('',
    (r'^robots.txt$', 'django.views.static.serve', 
      { 'path' : "/robots.txt", 
        'document_root': settings.TEMPLATE_DIRS[0],
        'show_indexes': False } ),
    (r'^favicon.ico$', 'django.views.static.serve', 
      { 'path' : "/favicon.ico", 
        'document_root': settings.TEMPLATE_DIRS[0],
        'show_indexes': False } ),
    (r'^css/(?P<path>.*)$', 'django.views.static.serve',
      { 'document_root': "%s/css" % settings.TEMPLATE_DIRS[0]}),
    (r'^images/(?P<path>.*)$', 'django.views.static.serve',
      { 'document_root': "%s/images" % settings.TEMPLATE_DIRS[0]}),
    (r'^fonts/(?P<path>.*)$', 'django.views.static.serve',
      { 'document_root': "%s/fonts" % settings.TEMPLATE_DIRS[0]}),
    (r'^javascripts/(?P<path>.*)$', 'django.views.static.serve',
      { 'document_root': "%s/javascripts" % settings.TEMPLATE_DIRS[0]}),  
  )
