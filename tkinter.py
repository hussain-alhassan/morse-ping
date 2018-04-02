# from Tkinter import *

# master = Tk()

# # def doStuff(event = None):
# # 	global c
# # 	print "Stuff Happened"
# # 	c["text"] = c["text"] + '...'
# # 	b["text"] = "Don't click me again!"

# def boxEntered(Event = None):
# 	c["text"] = d.get()

# # b = Button(master, text="Save")
# # b.grid(column = 0, row = 0)
# # b.bind('<Button>', doStuff )
# # c = Label(master, text = "Some text here")
# # c.grid(column = 0, row = 1)
# d = Entry(master)
# d.grid(column = 0, row = 0)
# d.bind('<Return>', boxEntered)

# Button(master,text="+",width=3, action('+').grid(row=5, column=1)
# Button(master,text="7",width=3, action(7)).grid(row=1, column=0)
# Button(master,text="8",width=3, action(8)).grid(row=1, column=1)
# Button(master,text="9",width=3, action(9)).grid(row=1, column=2)
# Button(master,text="4",width=3, action(4)).grid(row=2, column=0)
# Button(master,text="5",width=3, action(5)).grid(row=2, column=1)
# Button(master,text="6",width=3, action(6)).grid(row=2, column=2)
# Button(master,text="1",width=3, action(1)).grid(row=3, column=0)
# Button(master,text="2",width=3, action(2)).grid(row=3, column=1)
# Button(master,text="3",width=3, action(3)).grid(row=3, column=2)
# Button(master,text="0",width=3, action(0)).grid(row=4, column=0)

# mainloop()

# tkinterDemo.py
# Paul Talaga
# March 21, 2018
# Demo of using tkinter to build a simple calculator.
from Tkinter import *

def bclicked(event = None):
  output['text'] = str(output['text']) + str(event.widget.value)
  
def calculate(event = None):
  output['text'] = eval(output['text'])
  
def clear(event = None):
  output['text'] = ""

master = Tk()

# Where the numbers & result will go
output = Label(master,text = "")
output.grid(column = 0, row = 0, columnspan = 3)

# Generate the numbers
buttons = []
for n in range(9):
  b = Button(master, text=str(n+1))
  b.grid(column = n % 3, row = n / 3 + 1)
  # Note value is not a member variable of the Button object, but in 
  # python we can add members at any time.
  # This allows all numbers to use the same callback, and it can find
  # what button was pressed.
  b.value = n + 1
  b.bind('<Button>', bclicked)
  buttons.append(b)
  
b = Button(master, text=0)
b.grid(column = 1, row = 4)
b.value = 0
b.bind('<Button>', bclicked)
buttons.append(b)
  
# Include the operator buttons
add = Button(master, text="+")
add.grid(column = 0, row = 5)
add.value = '+'
add.bind("<Button>", bclicked)

sub = Button(master, text="-")
sub.grid(column = 1, row = 5)
sub.value = '-'
sub.bind("<Button>", bclicked)

mul = Button(master, text="*")
mul.grid(column = 2, row = 5)
mul.value = '*'
mul.bind("<Button>", bclicked)

calc = Button(master, text="Enter")
calc.grid(column = 0, row = 6, columnspan=3)
calc.bind("<Button>", calculate)

cl = Button(master, text="Clear")
cl.grid(column = 0, row = 7, columnspan=3)
cl.bind("<Button>", clear)


mainloop()
  