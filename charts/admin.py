from django.contrib import admin
from charts.models import TextBlockEnIt

class TextBlockEnItAdmin(admin.ModelAdmin):
  pass
  
admin.site.register(TextBlockEnIt, TextBlockEnItAdmin)
