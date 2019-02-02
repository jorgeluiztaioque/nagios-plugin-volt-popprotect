#!/usr/bin/env python3
#-----------------------------------------------------------------------
# Nagios check AC power status in Volt POP Protect Devices
# Written by Jorge Luiz Taioque
# jorgeluiztaioque [at] gmail [dot] com
#
#-----------------------------------------------------------------------

__author__ = 'Jorge Luiz Taioque'
__version__= 1.0

from easysnmp import Session
import sys

ip = sys.argv[1]

#Alarm only PON ports that has more than this value (variable [alarm] value)

snmpSession = Session(hostname=ip, community='public', version=2)

mibPowerac = ".1.3.6.1.4.1.17095.1.3.13"

status = snmpSession.get(mibPowerac+'.0').value

if status == '1':
	print ("AC-OK")
	sys.exit(0)
else:
	print ("AC-DOWN")
	sys.exit(2)
