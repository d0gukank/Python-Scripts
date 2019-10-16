#!/usr/bin/env python
import nmap
import json

f = open('output.html','w')
subnet = '192.168.1.0/24'
ports_list = ['80','443']

ports = ','.join(str(x) for x in ports_list)
nm = nmap.PortScanner() 
res=nm.scan(hosts=subnet, arguments='-sS -p ' + ports)

for i in res["scan"]:
	if res["scan"][i]["tcp"][80]["state"] == "open" and res["scan"][i]["tcp"][443]["state"] == "false":
		f.write ("<a href=\"http://"+res["scan"][i]['addresses']['ipv4']+"\">"+res["scan"][i]['addresses']['ipv4']+":80</a>")
		f.write("<br><br>")
	if res["scan"][i]["tcp"][80]["state"] == "false" and res["scan"][i]["tcp"][443]["state"] == "open":
		f.write ("<a href=\"https://"+res["scan"][i]['addresses']['ipv4']+"\">"+res["scan"][i]['addresses']['ipv4']+":443</a>")
		f.write("<br><br>")
	if res["scan"][i]["tcp"][443]["state"] == "open" and res["scan"][i]["tcp"][443]["state"] == "open":
		f.write ("<a href=\"http://"+res["scan"][i]['addresses']['ipv4']+"\">"+res["scan"][i]['addresses']['ipv4']+":80</a>")
		f.write("<br>")
		f.write ("<a href=\"https://"+res["scan"][i]['addresses']['ipv4']+"\">"+res["scan"][i]['addresses']['ipv4']+":443</a>")
		f.write("<br><br>")
	else:
		pass

f.close()
