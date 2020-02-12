import socket

dlist="""almiraj.asd.com
almiraj-v2.asd.com
drone.infra-dev.asd.com
dev.web.infra-dev.asd.com
prod.web.infra-dev.asd.com
stage.web.infra-dev.asd.com
posmw.asd.com
"""
#print dlist.splitlines()
for x in dlist.splitlines():
	try:
		ip=socket.gethostbyname(x)
		print ip +" : "+ x
	except:
		pass
