#!/usr/bin/env python

from common.dbconnect import db_connect
from common.entities import KippoHoneypot
from canari.maltego.entities import IPv4Address
from canari.maltego.message import Label, Field, UIMessage
from canari.config import config
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
 label='HoneyMalt: Kippo IPs',
 description='Connects to Kippo Honeypots via MYSQL db',
 uuids=[ 'HoneyMalt.v2.Connect_to_Kippo' ],
 inputs=[ ( 'HoneyMalt', KippoHoneypot ) ],
 debug=False
)
def dotransform(request, response, config):
  host = request.value
  x = db_connect(host)
  try:
    cursor = x.cursor()
    query = ("select ip from sessions")
    cursor.execute(query)
    for ip in cursor:
      e = IPv4Address('%s' %(ip))
      e += Field('kippoip', host, displayname='Kippo IP')
      response += e
    return response
  except:
    return response + UIMessage(x)


def onterminate():
  cursor.close()
  x.close()
  exit(0)
