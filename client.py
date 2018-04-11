import time
import socket

#UDP_IP = "10.18.99.162"
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE = "Hello, World!"

binary = "00010001"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

for i in binary:
	if i == '0':
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
		sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
	if i == '1':
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
		time.sleep(3)
		sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
	time.sleep(10)
