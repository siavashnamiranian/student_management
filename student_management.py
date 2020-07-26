from tkinter import *

#windows
root = Tk()
root.title("student management")

username_var=StringVar()
label = Label( root, textvariable=var, relief=RAISED )

var.set("Hey!? How are you doing?")
label.pack()
root.mainloop()
