import urllib2
import simplejson
from datetime import datetime


def get_json_data(url):
  """request json data from a URL """
  req = urllib2.Request(url)
  opener = urllib2.build_opener()
  return simplejson.load(opener.open(req))
