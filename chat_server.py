from Tkinter import *

window = Tk()

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