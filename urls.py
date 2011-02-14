from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib.sites.models import Site
from django.conf import settings
from charts.models import OppVLastDate

from django.contrib import admin
admin.autodiscover()


last_date = OppVLastDate.objects.db_manager('opp').raw(OppVLastDate.raw_sql)[0]
extraction_date = last_date.last_date

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),

    # static media (not for production!)
    (r'^css/(?P<path>.*)$', 'django.views.static.serve',
      { 'document_root': '/Users/guglielmo/Workspace/op_indice/templates/css'}),
    (r'^images/(?P<path>.*)$', 'django.views.static.serve',
      { 'document_root': '/Users/guglielmo/Workspace/op_indice/templates/images'}),
    (r'^fonts/(?P<path>.*)$', 'django.views.static.serve',
      { 'document_root': '/Users/guglielmo/Workspace/op_indice/templates/fonts'}),
    (r'^javascripts/(?P<path>.*)$', 'django.views.static.serve',
      { 'document_root': '/Users/guglielmo/Workspace/op_indice/templates/javascripts'}),

    # static pages
    (r'^$', direct_to_template, { 'template': 'charts/home.html', 
                                  'extra_context': { 'openparlamento_url': settings.OPENPARLAMENTO_URL,
                                                     'extraction_date': extraction_date,
                                                     'fetch_s3_images': settings.FETCH_S3_IMAGES,
                                                     'current_site_domain': Site.objects.get_current().domain } }),  
    (r'^methodology/$', direct_to_template, { 'template': 'charts/methodology.html' }),  

    # complete charts
    (r'^deputati/$', 'charts.views.mps', 
      { 'type': 'Deputati', 'group_by': 'list',
        'openparlamento_url': settings.OPENPARLAMENTO_URL, 'extraction_date': extraction_date }),
    (r'^deputati/(?P<group_by>\w+)/$', 'charts.views.mps', 
      { 'type': 'Deputati', 
        'openparlamento_url': settings.OPENPARLAMENTO_URL, 'extraction_date': extraction_date }),    
    (r'^senatori/$', 'charts.views.mps', { 
        'type': 'Senatori', 'group_by': 'list',
        'openparlamento_url': settings.OPENPARLAMENTO_URL, 'extraction_date': extraction_date }),
    (r'^senatori/(?P<group_by>\w+)/$', 'charts.views.mps', { 
        'type': 'Senatori',
        'openparlamento_url': settings.OPENPARLAMENTO_URL, 'extraction_date': extraction_date }),    

    (r'^(?P<op_location_name>[\w \']+)/$', 
      'charts.views.location', { 'openparlamento_url': settings.OPENPARLAMENTO_URL, 
                                 'extraction_date': extraction_date,
                                 'fetch_s3_images': settings.FETCH_S3_IMAGES }),    
)
