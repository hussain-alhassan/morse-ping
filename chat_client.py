from Tkinter import *

window = Tk()

message = Text(window)
message.pack()

client = StringVar()
inputs = Entry(window, text=client)

inputs.pack(side=BOTTOM, fill=X)


def press_enter(event):
	toBinary = (' '.join(format(ord(x), 'b') for x in inputs.get()))

	get_inputs = '0'+toBinary
	print(get_inputs)
	message.insert(INSERT, '%s\n' % get_inputs)
	client.set('')
	return "break"

frame = Frame(window)
inputs.bind("<Return>", press_enter)
frame.pack

window.mainloop()