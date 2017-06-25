import socket
soket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST="192.168.1.21"
PORT= 1111
server_address = (HOST, PORT)
soket.bind(server_address)
print ('starting up on %s port %s' % server_address)
print "Kullanici bekleniyor."
soket.listen(5) #kac kullanici olacak belirliyoruz
baglanti,adres = soket.accept()
print "Bir baglanti kabul edildi.",adres
baglanti.send("HOSGELDINIZ EFENDIM")
data = baglanti.recv(1024)
print data
soket.close()
