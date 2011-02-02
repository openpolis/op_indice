from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^css/(?P<path>.*)$', 'django.views.static.serve',
      { 'document_root': '/Users/guglielmo/Workspace/op_indice/templates/css'}),
    (r'^images/(?P<path>.*)$', 'django.views.static.serve',
      { 'document_root': '/Users/guglielmo/Workspace/op_indice/templates/images'}),
    (r'^fonts/(?P<path>.*)$', 'django.views.static.serve',
      { 'document_root': '/Users/guglielmo/Workspace/op_indice/templates/fonts'}),

    (r'^$', 'charts.views.home'),  
    (r'^deputati/$', 'charts.views.deputati'),
    (r'^senatori/$', 'charts.views.senatori'),
)
