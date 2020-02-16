import subprocess 

file = open('d.list', 'r')
dlist = file.read().splitlines()
print dlist
l=list()
for x in dlist: 
    #address = "127.0.0." + str(ping) 
    res = subprocess.call(['ping', '-c', '3', x]) 
    if res == 0: 
        print( "ping to", x, "OK") 
        l.append(x)
    else:
        print( "fail ", x )
for s in l:
    print s
