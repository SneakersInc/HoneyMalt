#!/usr/bin/env python

import pygeoip
import os
from canari.maltego.message import Field, UIMessage, Label
from canari.maltego.entities import IPv4Address, Image
from ConfigParser import SafeConfigParser
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
    'dotransform'
]

#@superuser
@configure(
    label='HoneyMalt: Kippo GeoIP Lookup',
    description='Convert IP address into GeoIP location',
    uuids=[ 'HoneyMalt.v2.kippo_ip_2_geo' ],
    inputs=[ ( 'HoneyMalt', IPv4Address ) ],
    debug=False
)
def dotransform(request, response, config):
  
  conf = SafeConfigParser()
  conf.read('HoneyMalt.conf')
  geodbpath = conf.get('geoip', 'geoip_db').strip('\'')

  ip = request.value
  host = request.fields['kippodatabase']
  if not os.path.exists(geodbpath): 
    return response + UIMessage('Need local install of MaxMinds Geo IP database')
  gi = pygeoip.GeoIP(geodbpath)
  rec = gi.record_by_addr(ip)
  country = rec['country_name']
  ccode = rec['country_code'].lower()
  flag_path = 'http://flags.sneakersinc.net/' + ccode + '.png'
  e = Image(country)
  e.url = (flag_path)
  e += Field('kippoip', host, displayname='Kippo IP')
  response += e
  return response