from tkinter import *

root = Tk()
root.geometry("300x300")
root.title(" EMP DB ")

def Take_input():
	name = inputtxtName.get("1.0", "end-1c")
	print(name)
    usn = inputtxtUsn.get("1.0", "end-1c")
    print(usn)
l = Label(text = "Name")
inputtxtName = Text(root, height = 2,
				width = 25,
				bg = "light yellow")
inputtxtUsn = Text(root, height = 2,
				width = 25,
				bg = "light yellow")

Output = Text(root, height = 5,
			width = 25,
			bg = "light cyan")

Display = Button(root, height = 2,
				width = 20,
				text ="Show",
				command = lambda:Take_input())

l.pack()
inputtxtName.pack()
Display.pack()
Output.pack()

mainloop()
