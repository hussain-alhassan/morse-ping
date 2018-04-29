import socket
import time

#UDP_IP = "10.27.103.201"
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

    # Store all the timestamps in an array For comparison.
    timestamp_array.append(milli_sec)

    print('timestamp: '+str(milli_sec)+'\n')

    # Deletes the last 3 packets from the array/list.
    # [-1] means last item of the list. [-2] 2nd last item ...ect
    if ( (len(timestamp_array) > 14) and (((len(timestamp_array)-3)%14) == 0) and ( (timestamp_array[-1] - timestamp_array[-2]) < 50)  ):
      timestamp_array.remove(timestamp_array[-3])
      timestamp_array.remove(timestamp_array[-2])
      timestamp_array.remove(timestamp_array[-1])
      break # Stop receiving packets

  # Stores all binary of the message as (string). It might be very long string
  allBinary = ''
  for i in range(0,len(timestamp_array),2):
    
    if (i>0 and (i%7) == 0):
      print "\n"

    if ( (int(timestamp_array[i+1]) - int(timestamp_array[i])) < 50):
      print 'Delay between the 2 packets: '+str( int(timestamp_array[i+1]) - int(timestamp_array[i]) )
      allBinary += '0'
    else:
      print 'Delay between the 2 packets: '+str( int(timestamp_array[i+1]) - int(timestamp_array[i]) )
      allBinary += '1'

  # Takes each 8 bits & stores them in a list (allBinaryList) so it can convert from binary to str.
  allBinaryList = []
  for i in range(0,len(allBinary),7):
    allBinaryList += [allBinary[i:i+7]]

  # You made it yay. This guy converts from binary to string
  print 'Msg received: '+''.join([chr(int(x, 2)) for x in allBinaryList])

