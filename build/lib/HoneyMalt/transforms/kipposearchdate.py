#!/usr/bin/env python

from common.dbconnect import db_connect
from datetime import datetime
from common.entities import KippoHoneypot, KippoSession
from canari.maltego.entities import IPv4Address
from canari.maltego.message import Label, Field, UIMessage
from canari.easygui import multenterbox
from canari.framework import configure #, superuser

__author__ = 'catalyst256'
__copyright__ = 'Copyright 2014, Honeymalt Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'catalyst256'
__email__ = 'catalyst256@gmail.com'
__status__ = 'Development'

__all__ = [
    'dotransform',
    'onterminate'
]

#@superuser
@configure(
 label='HoneyMalt: Search for Sessions by Date Range',
 description='Connects to Kippo Honeypots via MYSQL db and searches for an IP address',
 uuids=[ 'HoneyMalt.v2.search_ip_by_date' ],
 inputs=[ ( 'HoneyMalt', KippoHoneypot ) ],
 debug=False
)
def dotransform(request, response, config):
  msg = 'Enter Start & End Date'
  title = 'Kippo search for sessions by date range'
  fieldNames = ["Start Date", "End Date"]
  fieldValues = []
  fieldValues = multenterbox(msg, title, fieldNames)
  if fieldValues[0] or fieldValues[1] != '':
    s_date = datetime.strptime(fieldValues[0], '%Y-%m-%d')
    e_date = datetime.strptime(fieldValues[1], '%Y-%m-%d')
  else:
    return response + UIMessage('Specify a start & end date')
  host = request.value
  x = db_connect(host)
  try:
    cursor = x.cursor()
    query = ("select * from sessions where starttime between %s and %s")
    cursor.execute(query, (s_date,e_date))
    for (id, starttime, endtime, sensor, ip, termsize, client) in cursor:
      e = KippoSession('%s' %(id))
      e.starttime = ('%s' %(starttime))
      e.endtime = ('%s' %(endtime))
      e.sensor = ('%s' %(sensor))
      e.ipaddr =  ('%s' %(ip))
      e.termsize =  ('%s' %(termsize))
      e.client = ('%s' %(client))
      e += Field('kippoip', host, displayname='Kippo IP')
      response += e
    return response
  except:
    return response + UIMessage(x)

def onterminate():
  cursor.close()
  x.close()
  exit(0)
