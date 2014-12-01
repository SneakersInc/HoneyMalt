#!/usr/bin/env python

from common.dbconnect import db_connect
from common.entities import KippoSession, KippoInput
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
    label='HoneyMalt: Kippo Input',
    description='Get Kippo input based on sessions',
    uuids=['HoneyMalt.v2.Kippo_2_Input'],
    inputs=[('HoneyMalt', KippoSession)],
    debug=False
)
def dotransform(request, response):
    sess = request.value
    host = request.fields['kippodatabase']
    x = db_connect(host)
    try:
        cursor = x.cursor()
        query = "select timestamp, success, input from input where session like %s"
        cursor.execute(query, (sess,))
        for (timestamp, success, input) in cursor:
            e = KippoInput(input)
            e += Field('inputtime', timestamp, displayname='Time Stamp')
            e += Field('inputsuc', success, displayname='Success')
            e += Field('kippodatabase', host, displayname='Kippo Database')
            response += e
        return response
    except Exception as e:
        return response + UIMessage(str(e))
