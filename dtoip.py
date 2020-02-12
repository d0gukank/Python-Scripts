import socket

dlist="""almiraj.dhhmena.com
almiraj-v2.dhhmena.com
drone.infra-dev.dhhmena.com
dev.web.infra-dev.dhhmena.com
prod.web.infra-dev.dhhmena.com
stage.web.infra-dev.dhhmena.com
posmw.dhhmena.com
"""
#print dlist.splitlines()
for x in dlist.splitlines():
	try:
		ip=socket.gethostbyname(x)
		print ip +" : "+ x
	except:
		pass
