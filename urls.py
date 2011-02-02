from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),

    # static media (not for production!)
    (r'^css/(?P<path>.*)$', 'django.views.static.serve',
      { 'document_root': '/Users/guglielmo/Workspace/op_indice/templates/css'}),
    (r'^images/(?P<path>.*)$', 'django.views.static.serve',
      { 'document_root': '/Users/guglielmo/Workspace/op_indice/templates/images'}),
    (r'^fonts/(?P<path>.*)$', 'django.views.static.serve',
      { 'document_root': '/Users/guglielmo/Workspace/op_indice/templates/fonts'}),

    # static pages
    (r'^$', direct_to_template, { 'template' : 'charts/home.html' }),  
    (r'^methodology/$', direct_to_template, { 'template' : 'charts/methodology.html' }),  

    # complete charts
    (r'^deputati/$', 'charts.views.mps', { 'type': 'Deputati', 'group_by': 'list' }),
    (r'^deputati/(?P<group_by>\w+)/$', 'charts.views.mps', { 'type': 'Deputati' }),    
    (r'^senatori/$', 'charts.views.mps', { 'type': 'Senatori', 'group_by': 'list' }),
    (r'^senatori/(?P<group_by>\w+)/$', 'charts.views.mps', { 'type': 'Senatori' }),    
)
