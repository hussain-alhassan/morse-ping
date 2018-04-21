from Tkinter import *
import socket
import time

window = Tk()
#UDP_IP = "10.18.99.162"

UDP_IP = "127.0.0.1"

UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

data = True
timestamp_array = []
while data:
  data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes

  # Gets the timestamp in milli sec
  milli_sec = int(round(time.time() * 1000))

  # (to be more accurate), [:12] means take the 12 of 13 digits of timestamp
  milli_sec = str(milli_sec)[:12]

  # Store all the timestamps in an array For comparison.
  timestamp_array.append(milli_sec)

  print('timestamp: '+milli_sec+'\n')



message = Text(window)
message.pack()

server = StringVar()
inputs = Entry(window, text=server)
inputs.pack(side=BOTTOM, fill=X)

def press_enter(event):
	get_inputs = inputs.get()
	print(get_inputs)
	message.insert(INSERT, '%s\n' % get_inputs)
	server.set('')
	return "break"

frame = Frame(window)
inputs.bind("<Return>", press_enter)
frame.pack

window.mainloop()