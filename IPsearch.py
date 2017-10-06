#!/usr/bin/env python
import geoip2.database
import socket
import time
import sys
import os
import urllib2

if os.name in['nt','win32']:
	os.system('cls')
else:
	os.system('clear')
repeat='yes'
while repeat == 'yes' or repeat == 'yes':
	try:
		print "\n[*] Ip Address Tracker Location By p1d0f [*] "
		print "[*] Powered By Zorgon Team 		 [*]\n"
		inputIP=raw_input('[*] target host : ')
		print "[*] connecting to Internet ...."
		time.sleep(2)
		urllib2.urlopen("http://lb-192-30-255-113-sea.github.com", timeout=5)
		print "[*] Internet Connected [*]"
		dnsdomain=socket.gethostbyname(inputIP)
		print "[*] IP address : ",dnsdomain
		reader=geoip2.database.Reader('database/GeoLite2-City.mmdb')
		#isp=geoip2.database.Reader('database/GeoIP2-ISP.mmdb')
		response=reader.city("%s" % (dnsdomain))
		city=response.country.name
		code=response.country.iso_code
		city2=response.country.name
		name=response.subdivisions.most_specific.name
		code2=response.subdivisions.most_specific.iso_code
		city3=response.city.name
		postal=response.postal.code
		latitude=response.location.latitude
		logtitude=response.location.longitude
		for i in(5,4,3,2,1):
			time.sleep(2)
			print "[*] searching Ip Address ..."
		print "\n[*] City 	: ",city
		print "[*] Code 	: ",code
		print "[*] Country 	: ",city2
		print "[*] Divisi	: ",name
		print "[*] iso Code	: ",code2
		print "[*] City Name	: ",city3
		print "[*] postal code	: ",postal
		print "[*] Latitude	: ",latitude
		print "[*] Longtitude	: ",logtitude,"\n"
		for i in(5,4,3,2,1):
			time.sleep(1)
			print "[*] Searching ISP Connected ..."
		ispa=geoip2.database.Reader('database/GeoIP2-ISP.mmdb')
		connect=ispa.isp("%s" % (dnsdomain))
		isp1=connect.autonomous_system_number
		isp2=connect.autonomous_system_organization
		isp3=connect.isp
		#isp4=connect.organization
		isp5=connect.ip_address
		
		print "\n[*] Code Of ISP 	: ",isp1
		print "[*] Organization Of ISP	: ",isp2 
		print "[*] Name Of ISP		: ",isp3
		print "[*] Ip Address of ISP	: ",isp5
		
		print "\n[*] Done Happy Tracking [*]"
		reader.close()
   	
	except KeyboardInterrupt:
		print "\n[*] CTRL+C Activated"
		sys.exit()
	except urllib2.URLError as err:
		print "[*] Internet Diconnected [*]"
		sys.exit()
	except:
		#time.sleep(1)
		print "[*] Not Found Location"
		time.sleep(2)
			

