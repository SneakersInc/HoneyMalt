#!/usr/bin/env python
import mysql.connector
from mysql.connector import errorcode
from canari.config import config

__author__ = 'catalyst256'
__copyright__ = 'Copyright 2014, Honeymalt Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'catalyst256'
__email__ = 'catalyst256@gmail.com'
__status__ = 'Development'

def db_connect(host):
  # Try to connect to host on specified port
  # database = config['database/database']
  # username = config['database/username']
  # password = config['database/password']
  # username = config['database/username']

  database = 'kippo'
  username = 'kippo'
  password = 'Kippo-DB-pass'
  

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
      print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database does not exists")
    else:
      print(err)
  else:
    return cnx
