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

class KippoHoneypot(HoneymaltEntity):
    pass

class KippoLogin(HoneymaltEntity):
    pass

@EntityField(name='HoneyMalt.client', propname='client', displayname='Client')
@EntityField(name='HoneyMalt.termsize', propname='termsize', displayname='Term Size')
@EntityField(name='HoneyMalt.ipaddr', propname='ipaddr', displayname='IP Address')
@EntityField(name='HoneyMalt.sensor', propname='sensor', displayname='Sensor')
@EntityField(name='HoneyMalt.endtime', propname='endtime', displayname='End Time')
@EntityField(name='HoneyMalt.starttime', propname='starttime', displayname='Start Time')
class KippoSession(HoneymaltEntity):
    pass

class KippoInput(HoneymaltEntity):
    pass
