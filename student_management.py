from tkinter import *
import tkinter.ttk as ttk
import sqlite3
from sqlite3 import Error

#windows
class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("student management")
        self.root.geometry("250x100")

        #user name label and entry
        label = Label( root, text="user name:")

        self.username_var=StringVar()
        entry=Entry(root,textvariable=self.username_var)

        label.grid(row=0,column=0)
        entry.grid(row=0,column=1)

        #password label and entry
        label_pass = Label( root, text="password:")

        self.password=StringVar()
        entry_pass=Entry(root,textvariable=self.password,show="*")

        label_pass.grid(row=1,column=0)
        entry_pass.grid(row=1,column=1)
        #login button
        login_btn = Button(root, text = 'log in', command = self.secondScreen)
        login_btn.grid(row=2,column=0)
        #register button
        register_btn = Button(root, text = 'register', command = root.destroy)
        register_btn.grid(row=2,column=1)
    def secondScreen(self):
        root2 = Toplevel(self.root)
        enter = EnterData(root)
class EnterData:
    def __init__(self,root):
        self.root = root
        self.root.geometry('800x500')
        self.root.title("Student Management(Enter Data)")
        self.name = StringVar()
        self.dob = StringVar()
        self.roll = StringVar()
        self.gen = StringVar()



if __name__ == "__main__":
    root = Tk()
    l = login_window(root)
    root.mainloop()