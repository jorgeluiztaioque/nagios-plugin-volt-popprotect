#!/usr/bin/env python3
#-----------------------------------------------------------------------
# Nagios check Imput battery voltage in Volt POP Protect Devices
# Written by Jorge Luiz Taioque
# jorgeluiztaioque [at] gmail [dot] com
#
#-----------------------------------------------------------------------

__author__ = 'Jorge Luiz Taioque'
__version__= 1.0

from easysnmp import Session
import sys

def main(argv):
	if not argv:
		print ('Uso:')
		print ('./check_battery_voltage.py [ipaddress] [voltagem_minima] [voltagem_maxima]')
		print ('./check_battery_voltage.py 10.0.0.1 11 14')
	else:

		ip = sys.argv[1]
		voltageLow = sys.argv[2]
		voltageHigh = sys.argv[3]

		voltageMargin = 3

		voltageLow = float(voltageLow)
		voltageHigh = float(voltageHigh)

		snmpSession = Session(hostname=ip, community='public', version=2)

		mibBatteryVoltage = ".1.3.6.1.4.1.17095.1.3.12"

		status = snmpSession.get(mibBatteryVoltage+'.0').value

		sts = (float(status)/10)

		if sts == 0:
			print ("No battery voltage")
			sys.exit(2)
		if sts >= 120:
			print ("No battery voltage")
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

if __name__ =='__main__':
    main(sys.argv[1:])
