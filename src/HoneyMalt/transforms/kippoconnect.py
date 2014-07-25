#!/usr/bin/env python
import socket
from common.dbconnect import db_connect
from common.entities import Database, KippoHoneypot
from canari.maltego.message import Label, Field
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
    'dotransform'
]

#@superuser
@configure(
 label='HoneyMalt: Connect Database',
 description='Connects to MySQL Database for Kippo Honeypots',
 uuids=[ 'HoneyMalt.v2.Connect_to_Database' ],
 inputs=[ ( 'HoneyMalt', Database ) ],
    debug=True
)
def dotransform(request, response, config):
 host = request.value
 x = db_connect(host)
 print x
 return response
