from django import template
from charts.models import OppVIndicePolitico
import datetime
from dateutil.parser import *

register = template.Library()

# usage: {% get_mps oftype deputati in params.constituency asof extraction_date as mps %}
def do_mps(parser, token):
  bits = token.split_contents()
  if len(bits) != 9:
    raise template.TemplateSyntaxError("'get_top' requires exactly 9 parameters")
  mp_type = bits[2]
  constituency = bits[4]
  date = bits[6]
  varname = bits[8]
    
  return MpsNode(mp_type, constituency, date, varname)
  
class MpsNode(template.Node):
  def __init__(self, mp_type, constituency, date, varname):
    self.tree = ''
    if (mp_type == 'deputati'):
      self.tree = 'C'
    if (mp_type == 'senatori'):
      self.tree = 'S'
    self.constituency = template.Variable(constituency)
    self.varname = varname
    self.extraction_date = template.Variable(date)
    print "type: %s" % mp_type
    
  def render(self, context):
    try:
      actual_extraction_date = self.extraction_date.resolve(context)    
      actual_constituency = self.constituency.resolve(context)
      context[self.varname] = OppVIndicePolitico.objects.db_manager('opp').raw(OppVIndicePolitico.raw_sqls['mps_in_location'], [actual_extraction_date, self.tree, actual_constituency])
      return ''
    except template.VariableDoesNotExist:
      return ''

register.tag('get_mps', do_mps)


# usage: {% get_top 5 deputati as mps asof dd/mm/yyyy %}
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

register.tag('get_top', do_top)
      
@register.filter
def multiply_by(value, multiplier):
  """multiply a value by the multiplier; both value and multiplier must be numbers"""
  return float(value) * float(multiplier)
  
  
  



