import socket
import time

#UDP_IP = "10.18.99.162"
#UDP_IP = '10.18.98.54'
UDP_IP = "127.0.0.1"

UDP_PORT = 5005
 
sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True: 
  data = True
  timestamp_array = []
  while data:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes

    # Gets the timestamp in milli sec
    milli_sec = int(round(time.time() * 1000))

    # (to be more accurate), [:12] means take the 12 of 13 digits of timestamp
    #milli_sec = str(milli_sec)[:13]
    #milli_sec = str(milli_sec)

    # Store all the timestamps in an array For comparison.
    timestamp_array.append(milli_sec)

    print('timestamp: '+str(milli_sec)+'\n')

    # Deletes the last 3 packets from the array/list.
    # [-1] means last item of the list. [-2] 2nd last item ...ect
    if ( (len(timestamp_array) > 14) and (((len(timestamp_array)-3)%14) == 0) and ( (timestamp_array[-1] - timestamp_array[-2]) < 50)  ):
      print "inside"
      x = (timestamp_array[-1] - timestamp_array[-2])
      print x
      #( timestamp_array[-1] == timestamp_array[-2] == timestamp_array[-3])):
      print 'packets # before'
      print len(timestamp_array)
      timestamp_array.remove(timestamp_array[-3])
      timestamp_array.remove(timestamp_array[-2])
      timestamp_array.remove(timestamp_array[-1])
      print 'packets # after'
      print len(timestamp_array)
      break # Stop receiving packets

  # Stores all binary of the message as (string). It might be very long string
  allBinary = ''
  for i in range(0,len(timestamp_array),2):
    if ( (int(timestamp_array[i+1]) - int(timestamp_array[i])) < 50):
      allBinary += '0'
    else:
      allBinary += '1'

  # Takes each 8 bits & stores them in a list (allBinaryList) so it can convert from binary to str.
  allBinaryList = []
  print 'length: '+str(len(allBinary))
  for i in range(0,len(allBinary),7):
    allBinaryList += [allBinary[i:i+7]]

  print allBinary
  # You made it yay. This guy converts from binary to string
  print ''.join([chr(int(x, 2)) for x in allBinaryList])

