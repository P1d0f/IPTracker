#!/usr/bin/env python

from geopy.geocoders import Nominatim
import sys
import time

repeat='yes'
while repeat == 'yes' or repeat == 'yes':
	print "\n[*] Geolocation By Mizan [*]"
	try:
		inputCity=raw_input("[*] Address Or City : ")
		geolocator=Nominatim()
		location=geolocator.geocode("%s" % (inputCity))
		for i in(5,4,3,2,1):
			time.sleep(2)
			print "[*] Searching ...."
		#time.sleep(2)
		print
		res=location.address
		res2=location.latitude,location.longitude
		print "[*] Location By Address : ", res
		print "[*] Location By LatLong : ", res2
	
	except KeyboardInterrupt:
		print "\n[*] CTRL+C active"
		sys.exit()
	except :
		print "[*] Not Found Address"
