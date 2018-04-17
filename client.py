import time
import socket


#UDP_IP = "10.18.99.162"
UDP_IP = "127.0.0.1"

UDP_PORT = 5005
MESSAGE = "packet 1"
MESSAGE3 = "packet 2"

MESSAGE2 = "ab"
 
for i in MESSAGE2:
	my8bits = '0'+' '.join(format(ord(x), 'b') for x in i)
	#my8bits = '010'
	print my8bits # this guy will have 8 bits each time
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
		time.sleep(0.1)
	time.sleep(3)

sock.sendto('p1_end', (UDP_IP, UDP_PORT))
sock.sendto('p2_end', (UDP_IP, UDP_PORT))
sock.sendto('p3_end', (UDP_IP, UDP_PORT))
	# End of the first letter
	