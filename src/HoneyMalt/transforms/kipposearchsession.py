#!/usr/bin/env python

from common.dbconnect import db_connect
from common.entities import KippoHoneypot
from canari.maltego.entities import IPv4Address
from canari.maltego.message import Field
from canari.framework import configure

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
    label='HoneyMalt: Kippo IPs',
    description='Connects to Kippo Honeypots via MYSQL db',
    uuids=['HoneyMalt.v2.Connect_to_Kippo'],
    inputs=[('HoneyMalt', KippoHoneypot)],
    debug=False
)
def dotransform(request, response):
    host = request.fields['kippodatabase']
    x = db_connect(host)
    cursor = x.cursor()
    query = "select ip from sessions"
    cursor.execute(query)
    for ip in cursor:
        e = IPv4Address('%s' % ip)
        e += Field('kippodatabase', host, displayname='Kippo Database')
        response += e
    return response

