#!/usr/bin/env python3
#-----------------------------------------------------------------------
# Nagios check Imput ac voltage in Volt POP Protect Devices
# Written by Jorge Luiz Taioque
# jorgeluiztaioque [at] gmail [dot] com
#
#-----------------------------------------------------------------------

__author__ = 'Jorge Luiz Taioque'
__version__= 1.0

from easysnmp import Session
import sys

ip = sys.argv[1]
voltageLow = sys.argv[2]
voltageHigh = sys.argv[3]

voltageMargin = 3

#Alarm only PON ports that has more than this value (variable [alarm] value)
voltageLow = float(voltageLow)
voltageHigh = float(voltageHigh)

snmpSession = Session(hostname=ip, community='public', version=2)

mibImputVoltage = ".1.3.6.1.4.1.17095.1.3.11"

status = snmpSession.get(mibImputVoltage+'.0').value

sts = (float(status)/10)

if sts == 0:
	print ("No imput voltage")
	sys.exit(2)
if sts >= 120:
	print ("No imput voltage")
	sys.exit(2)
if sts >= voltageLow and sts <= voltageHigh:
	print ("Voltage OK= "+str(sts))
	sys.exit(0)
if sts >= (voltageLow-voltageMargin) and sts < voltageLow:
	print ("Voltage Warning low= "+str(sts))
	sys.exit(1)
if sts > voltageHigh and sts < (voltageHigh+voltageMargin):
	print ("Voltage Warning high= "+str(sts))
	sys.exit(1)
if sts < (voltageLow-voltageMargin):
	print ("Voltage Low= "+str(sts))
	sys.exit(2)
if sts > (voltageHigh+voltageMargin):
	print ("Voltage High= "+str(sts))
	sys.exit(2)
