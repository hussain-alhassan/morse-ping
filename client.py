import time
import socket
from Tkinter import *
from random import randint

window = Tk()
message = Text(window)
message.pack()

class ABC(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()

window = ABC(master=window)
window.master.title("Client")
client = StringVar()
inputs = Entry(window, text=client)
inputs.pack(side=BOTTOM, fill=X)

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

def mySocket(real_msg):
	print 'Secretly sending: '+real_msg 
	for i in real_msg:
		my7bits = ' '.join(format(ord(x), 'b') for x in i) #changed my8bits to my7bits; ascii characters only have 7 bits, NOT 8
		#see this ascii table to view # of bits for each char https://upload.wikimedia.org/wikipedia/commons/d/dd/ASCII-Table.svg

		#spaces and non-alphabetical characters only have 6 digits in binary; adds 0 to beginning of any chars with less than 7 digits in binary
		if len(my7bits) < 7:
			my7bits = '0'+my7bits

		#my7bits = '010'
		print my7bits+' ======== '+i # this guy will have 7 bits each time. (i) shows the current letter
		for bit in my7bits:
			msg = str(randint(0, 1000000))
			if bit == '0':
				sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
				sock.sendto(msg, (UDP_IP, UDP_PORT))
				sock.sendto(msg, (UDP_IP, UDP_PORT))
			if bit == '1':
				sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
				sock.sendto(msg, (UDP_IP, UDP_PORT))
				time.sleep(0.1)
				sock.sendto(msg, (UDP_IP, UDP_PORT))
			time.sleep(0.1) # End of the first letter. Wait then continue
		time.sleep(0.3) # End of sending the message
	# When the msg is done, send 3 packets in a row (Signal means done)
	sock.sendto('p1_end', (UDP_IP, UDP_PORT))
	sock.sendto('p2_end', (UDP_IP, UDP_PORT))
	sock.sendto('p3_end', (UDP_IP, UDP_PORT))

def press_enter(event):
	real_msg = inputs.get()
	message.insert(INSERT, '%s\n' % real_msg)
	client.set('')
	mySocket(real_msg)
	return "break"

frame = Frame(window)
inputs.bind("<Return>", press_enter)

frame.pack

window.mainloop()