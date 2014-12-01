#!/usr/bin/env python

from common.dbconnect import db_connect
from common.entities import KippoHoneypot, KippoDatabase
from canari.maltego.message import Field, UIMessage
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
    label='HoneyMalt: Kippo Sensors',
    description='Connects to Kippo Honeypots via MYSQL db',
    uuids=['HoneyMalt.v2.Get_Kippo_Sensors'],
    inputs=[('HoneyMalt', KippoDatabase)],
    debug=True
)
def dotransform(request, response):
    host = request.value
    x = db_connect(host)
    try:
        cursor = x.cursor()
        query = "select * from sensors"
        cursor.execute(query)
        for (id, ip) in cursor:
            e = KippoHoneypot('%s' % ip)
            e += Field('kippodatabase', host, displayname='Kippo Database')
            e += Field('kipposensorid', ('%s' % id), displayname='Kippo Sensor ID')
            response += e
        return response
    except Exception as e:
        return response + UIMessage(str(e))
