from django import template
from charts.models import OppVIndicePolitico
import datetime
from dateutil.parser import *

# usage: {% get_top 5 deputati as top_five_deputati asof dd/mm/yyyy %}
def do_top(parser, token):
  bits = token.split_contents()
  if len(bits) != 7:
    raise template.TemplateSyntaxError("'get_top' requires exactly 7 parameters")
  num = bits[1]
  mp_type = bits[2]
  varname = bits[4]
  date = bits[6]
    
  return TopNode(num, mp_type, varname, date)
  
class TopNode(template.Node):
  def __init__(self, num, mp_type, varname, date):
    self.num = int(num)
    self.varname = varname
    self.tree = ''
    if (mp_type == 'deputati'):
      self.tree = 'C'
    if (mp_type == 'senatori'):
      self.tree = 'S'
    self.extraction_date = template.Variable(date)
    
  def render(self, context):
    try:
      actual_extraction_date = self.extraction_date.resolve(context)    
      context[self.varname] = OppVIndicePolitico.objects.db_manager('opp').raw(OppVIndicePolitico.raw_sqls['top'], [actual_extraction_date, self.tree, self.num])
      return ''
    except template.VariableDoesNotExist:
      return ''

register = template.Library()
register.tag('get_top', do_top)
      
@register.filter
def multiply_by(value, multiplier):
  """multiply a value by the multiplier; both value and multiplier must be numbers"""
  return float(value) * float(multiplier)


