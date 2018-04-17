import socket
import time

#UDP_IP = "10.18.99.162"

UDP_IP = "127.0.0.1"


UDP_PORT = 5005
 
sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
 
print '\n'
data = True
timestamp_array = []
while data:
  data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
  #print "received message:", data


  milli_sec = int(round(time.time() * 1000))
  milli_sec_10_digits = str(milli_sec)[:10]
  timestamp_array.append(milli_sec_10_digits)

  #print('timestamp: '+milli_sec_10_digits+'\n')


  if (len(timestamp_array) >2 and 
    (timestamp_array[-1] == timestamp_array[-2] == timestamp_array[-3])):
    timestamp_array.remove(timestamp_array[-3])
    timestamp_array.remove(timestamp_array[-2])
    timestamp_array.remove(timestamp_array[-1])
    break



msg_array = []
for i in range(0,len(timestamp_array),2):
  if (timestamp_array[i] == timestamp_array[i+1]):
    #msg_array.append(0)
    print 0
  else:
    #msg_array.append(1)
    print 1
