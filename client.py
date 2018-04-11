import time
import socket


UDP_IP = "10.18.99.162"
#UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE = "packet 1"
MESSAGE3 = "packet 2"

MESSAGE2 = "a"
 
for i in MESSAGE2:
	my8bits = '0'+' '.join(format(ord(x), 'b') for x in i)
	print my8bits
	for bit in my8bits:
		if bit == '0':
			sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
			sock.sendto(MESSAGE3, (UDP_IP, UDP_PORT))
		if bit == '1':
			sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
			time.sleep(1)
			sock.sendto(MESSAGE3, (UDP_IP, UDP_PORT))
		time.sleep(3)





'''
for i in range(10):
	st = "hello world"
	' '.join(format(ord(x), 'b') for x in st)



	sock.sendto(str(i), (UDP_IP, UDP_PORT))

#sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

'''

