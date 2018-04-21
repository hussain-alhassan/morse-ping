from Tkinter import *
import time
import socket


#UDP_IP = "10.18.99.162"
UDP_IP = "127.0.0.1"

UDP_PORT = 5005
msg_packet1 = "packet 1"
msg_packet2 = "packet 2"

window = Tk()

message = Text(window)
message.pack()

client = StringVar()
inputs = Entry(window, text=client)

inputs.pack(side=BOTTOM, fill=X)

welcome = "Please enter a message:"

def press_enter(event):
	print welcome
	# toBinary = (' '.join(format(ord(x), 'b') for x in inputs.get()))
	#my8bits = '0'+' '.join(format(ord(x), 'b') for x in i)

	#my8bits = '010'
	#print my8bits+' ======== '+i # this guy will have 8 bits each time. (i) shows the current letter

	'''for bit in my8bits:
		if bit == '0':
			sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			sock.sendto(msg_packet1, (UDP_IP, UDP_PORT))
			sock.sendto(msg_packet2, (UDP_IP, UDP_PORT))
		if bit == '1':
			sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			sock.sendto(msg_packet1, (UDP_IP, UDP_PORT))
			time.sleep(1)
			sock.sendto(msg_packet2, (UDP_IP, UDP_PORT))
		time.sleep(0.1) # End of the first letter. Wait then continue
	time.sleep(3) # End of sending the message
	'''
	print(real_msg)
	message.insert(INSERT, '%s\n' % real_msg)
	client.set('')
	return "break"
'''
	sock.sendto('p1_end', (UDP_IP, UDP_PORT))
	sock.sendto('p2_end', (UDP_IP, UDP_PORT))
	sock.sendto('p3_end', (UDP_IP, UDP_PORT))
'''
# When the msg is done, send 3 packets in a row (Signal means done)


	#get_inputs = '0'+toBinary
	

frame = Frame(window)
inputs.bind("<Return>", press_enter)
frame.pack

window.mainloop()	