#!/usr/bin/env python3
#-----------------------------------------------------------------------
# Nagios check External Temperature in Volt POP Protect Devices
# Written by Jorge Luiz Taioque
# jorgeluiztaioque [at] gmail [dot] com
#
#-----------------------------------------------------------------------

__author__ = 'Jorge Luiz Taioque'
__version__= 1.0

from easysnmp import Session
import sys

ip = sys.argv[1]
tempMidle = sys.argv[2]
tempHigh = sys.argv[3]

#Alarm only PON ports that has more than this value (variable [alarm] value)
tempMidle = int(tempMidle)
tempHigh = int(tempHigh)

snmpSession = Session(hostname=ip, community='public', version=2)

mibExtTemp = ".1.3.6.1.4.1.17095.1.3.10"

status = snmpSession.get(mibExtTemp+'.0').value

sts = int(status)

if sts < tempMidle:
	print ("Temp_Sensor_OK="+status)
	sys.exit(0)
if sts >= (tempMidle) and sts < tempHigh:
	print ("Temp_Sensor_Warning="+status)
	sys.exit(1)
if sts >= tempHigh and sts < 254:
	print ("Temp_Sensor_High="+status)
	sys.exit(2)
if sts == 0:
	print ("External Sensor is not present")
	sys.exit(2)
if sts >= 125:
	print ("External Sensor is not present")
	sys.exit(2)
