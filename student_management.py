from tkinter import *

#windows
root = Tk()
root.title("student management")

username_var=StringVar()
label = Label( root, textvariable=username_var, relief=RAISED )

username_var.set("Hey!? How are you doing?")
label.pack()
root.mainloop()
