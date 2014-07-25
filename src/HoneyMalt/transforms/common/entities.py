#!/usr/bin/env python

from canari.maltego.message import Entity, EntityField, EntityFieldType, MatchingRule

__author__ = 'catalyst256'
__copyright__ = 'Copyright 2014, Honeymalt Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'catalyst256'
__email__ = 'catalyst256@gmail.com'
__status__ = 'Development'

__all__ = [
    'HoneymaltEntity',
    'MyHoneymaltEntity'
]

class HoneymaltEntity(Entity):
    _namespace_ = 'HoneyMalt'

#@EntityField(name='HoneyMalt.fieldN', propname='fieldN', displayname='Field N', matchingrule=MatchingRule.Loose)
#@EntityField(name='HoneyMalt.field1', propname='field1', displayname='Field 1', type=EntityFieldType.Integer)
class KippoHoneypot(HoneymaltEntity):
    pass

class Database(HoneymaltEntity):
    pass