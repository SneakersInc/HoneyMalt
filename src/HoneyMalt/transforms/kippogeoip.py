#!/usr/bin/env python

import pygeoip
import os
from canari.maltego.message import Field, UIMessage, Label
from canari.maltego.entities import IPv4Address, Image
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
  ip = request.value
  host = request.fields['kippoip']
  if not os.path.exists('/opt/geoip/GeoLiteCity.dat'): 
    return response + UIMessage('Need local install of MaxMinds Geo IP database')
  gi = pygeoip.GeoIP('/opt/geoip/GeoLiteCity.dat')
  rec = gi.record_by_addr(ip)
  country = rec['country_name']
  ccode = rec['country_code'].lower()
  flag_path = 'http://flags.sneakersinc.net:8080/' + ccode + '.png'
  e = Image(country)
  e.url = (flag_path)
  e += Field('kippoip', host, displayname='Kippo IP')
  response += e
  return response