import socket
import time

#UDP_IP = "10.18.99.162"

UDP_IP = "127.0.0.1"


UDP_PORT = 5005
 
sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
 
print '\n'
while True:
  data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
  print "received message:", data
  milli_sec = int(round(time.time() * 1000))
  if (data == 'packet 1'):
  	milli_sec_packet1 = int(round(time.time() * 1000))
  	print('p1_timestamp: '+str(milli_sec_packet1)[:10])
  elif (data == 'packet 2'):
  	milli_sec_packet2 = int(round(time.time() * 1000))
  	print('p2_timestamp: '+str(milli_sec_packet2)[:10])

  	if (str(milli_sec_packet1)[:10] == str(milli_sec_packet2)[:10]):
  		print 'bit = 0\n'
  	else:
  		print 'bit = 1\n'
