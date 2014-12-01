#!/usr/bin/env python

import mysql.connector
from mysql.connector import errorcode
from ConfigParser import SafeConfigParser

__author__ = 'catalyst256'
__copyright__ = 'Copyright 2014, Honeymalt Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'catalyst256'
__email__ = 'catalyst256@gmail.com'
__status__ = 'Development'


def db_connect(host):
    conf = SafeConfigParser()
    conf.read('HoneyMalt.conf')
    database = conf.get('kippodb', 'database').strip('\'')
    username = conf.get('kippodb', 'username').strip('\'')
    password = conf.get('kippodb', 'password').strip('\'')
  
    config = {
        'user': username,
        'password': password,
        'host': host,
        'database': database,
        'raise_on_warnings': True,
    }
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            return "Something is wrong with your user name or password"
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            return "Database does not exists"
        else:
            return err
    else:
        return cnx
