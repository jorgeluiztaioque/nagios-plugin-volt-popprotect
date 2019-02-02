#!/usr/bin/env python3
#-----------------------------------------------------------------------
# Nagios check Alarm Status in Volt POP Protect Devices
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
		print ('./check_active-alarm.py [ipaddress]')
		print ('./check_active-alarm.py 10.0.0.1')
	else:

		ip = sys.argv[1]

		#Alarm only PON ports that has more than this value (variable [alarm] value)

		snmpSession = Session(hostname=ip, community='public', version=2)

		mibAlarm = ".1.3.6.1.4.1.17095.1.3.8"

		status = snmpSession.get(mibAlarm+'.0').value

		if status == '1':
			print ("ALARME-ATIVO")
			sys.exit(0)
		else:
			print ("ALARME-DESATIVADO")
			sys.exit(2)

if __name__ =='__main__':
    main(sys.argv[1:])
