import socket
soket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST = "192.168.1.21"
PORT = 1111
soket.connect((HOST,PORT))
data = soket.recv(1024)
print data
soket.send("hosbulduk")
soket.close()
