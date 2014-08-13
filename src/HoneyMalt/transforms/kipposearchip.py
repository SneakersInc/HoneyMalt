#!/usr/bin/env python

from common.dbconnect import db_connect
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
 label='HoneyMalt: Search for Sessions by IP',
 description='Connects to Kippo Honeypots via MYSQL db and searches for an IP address',
 uuids=[ 'HoneyMalt.v2.search_ip_4_sess' ],
 inputs=[ ( 'HoneyMalt', KippoHoneypot ) ],
 debug=False
)
def dotransform(request, response, config):
  msg = 'Enter Search Criteria'
  title = 'Kippo search for sessions by IP'
  fieldNames = ["IP"]
  fieldValues = []
  fieldValues = multenterbox(msg, title, fieldNames)
  if fieldValues[0] != '':
    s_ip = fieldValues[0]
  else:
    return response + UIMessage('You need to type an IP address!!')
  host = request.value
  x = db_connect(host)
  cursor = x.cursor()
  query = ("select * from sessions where ip like %s")
  cursor.execute(query, (s_ip,))
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

def onterminate():
  cursor.close()
  x.close()
  exit(0)
