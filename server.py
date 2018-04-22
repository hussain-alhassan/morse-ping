import socket
import time
from Tkinter import *

# UDP_IP = "10.18.99.162"
UDP_IP = "127.0.0.1"

UDP_PORT = 5005

window = Tk()
message = Text(window)
message.pack()

class ABC(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()

window = ABC(master=window) 
window.master.title("Server")

myServer = StringVar()
inputs = Entry(window, text=myServer)

frame = Frame(window)
frame.pack
sock = socket.socket(socket.AF_INET,  # Internet
                         socket.SOCK_DGRAM)  # UDP
sock.bind((UDP_IP, UDP_PORT))
def mySocket():
    myData = ''
    while(1):
        data = True
        timestamp_array = []
        while data:
            if (myData):
                data = myData
                print 'emptying myData'
                myData = ''
            else:
                data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
            print 'data ' + data
            # Gets the timestamp in milli sec
            milli_sec = int(round(time.time() * 1000))

            # (to be more accurate), [:12] means take the 12 of 13 digits of timestamp
            milli_sec = str(milli_sec)[:12]

            # Store all the timestamps in an array For comparison.
            timestamp_array.append(milli_sec)

            print('timestamp: ' + milli_sec + '\n')

            # Deletes the last 3 packets from the array/list.
            # [-1] means last item of the list. [-2] 2nd last item ...ect
            if (len(timestamp_array) > 2 and
                    (timestamp_array[-1] == timestamp_array[-2] == timestamp_array[-3])):
                timestamp_array.remove(timestamp_array[-3])
                timestamp_array.remove(timestamp_array[-2])
                timestamp_array.remove(timestamp_array[-1])
                break  # Stop receiving packets

        # Stores all binary of the message as (string). It might be very long string
        allBinary = ''
        print 'length ' + str(len(timestamp_array))
        for i in range(0, len(timestamp_array), 2):
            if (timestamp_array[i] == timestamp_array[i + 1]):
                allBinary += '0'
            else:
                allBinary += '1'
        print allBinary
        # Takes each 8 bits & stores them in a list (allBinaryList) so it can convert from binary to str.
        allBinaryList = []
        for i in range(0, len(allBinary), 7):
            print 'anything'
            print [allBinary[i:i + 7]]
            allBinaryList += [allBinary[i:i + 7]]
        # You made it. yay. This guy converts from binary to string
        print 'END OF MESSAGE'
        print ''.join([chr(int(x, 2)) for x in allBinaryList])
        return ''.join([chr(int(x, 2)) for x in allBinaryList])
        myData = sock.recvfrom(1024)  # buffer size is 1024 bytes
print 'Note: Move the client window & server window will come after you enter the message'

real_msg = mySocket()
message.insert(INSERT, '%s\n' % real_msg)
myServer.set('')
data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
if data:
    real_msg = mySocket()
    message.insert(INSERT, '%s\n' % real_msg)
    myServer.set('')
window.mainloop()