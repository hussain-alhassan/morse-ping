from Tkinter import *

window = Tk()

message = Text(window)
message.pack()

client = StringVar()
inputs = Entry(window, text=client)

inputs.pack(side=BOTTOM, fill=X)

def press_enter(event):
	print 'our msg: '+inputs.get()

	client.set('')
	return "break"

frame = Frame(window)
inputs.bind("<Return>", press_enter)

frame.pack

window.mainloop()	