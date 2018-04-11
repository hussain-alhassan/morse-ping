import socket
import time
#UDP_IP = "127.0.0.1" 
UDP_IP = "10.18.99.162" 
UDP_PORT = 5005
MESSAGE = "a"
 
print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP



for i in MESSAGE:
	myBits = ' '.join(format(ord(x), 'b') for x in i)
	for bit in myBits:
		if (bit == '1'):
			print bit
			time.sleep(1)
			# send the next bit
		else:
			print bit


'''
for i in range(10):
	st = "hello world"
	' '.join(format(ord(x), 'b') for x in st)



	sock.sendto(str(i), (UDP_IP, UDP_PORT))

#sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

'''