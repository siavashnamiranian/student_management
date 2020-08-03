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
        label.grid(row=0,column=0)

        self.username_var=StringVar()
        entry=Entry(root,textvariable=self.username_var)
        entry.grid(row=0,column=1)
        
        #password label and entry
        label_pass = Label( root, text="password:")
        label_pass.grid(row=1,column=0)
        self.password=StringVar()
        entry_pass=Entry(root,textvariable=self.password,show="*")
        entry_pass.grid(row=1,column=1)
        
        #login button
        login_btn = Button(root, text = 'log in', command = self.secondScreen)
        login_btn.grid(row=2,column=0)
        #register button
        register_btn = Button(root, text = 'register', command = root.destroy)
        register_btn.grid(row=2,column=1)
    def secondScreen(self):
        root2 = Toplevel(self.root)
        enter = EnterData(root2)
class EnterData:
    def __init__(self,root):
        self.dataStart()
        self.root = root
        self.root.geometry('300x150')
        self.root.title("enter data")
        self.name = StringVar()
        self.dob = StringVar()
        self.roll = StringVar()
        self.gen = StringVar()
############gui#########
        # student name
        lbl_name=Label(self.root,text="student name:")
        lbl_name.grid(row=0,column=0)
        ent_name=Entry(self.root,textvariable=self.name)
        ent_name.grid(row=0,column=1)
        #roll no
        lbl_roll=Label(self.root,text="roll no:")
        lbl_roll.grid(row=1,column=0)
        ent_roll=Entry(self.root,textvariable=self.roll)
        ent_roll.grid(row=1,column=1)
        #dob
        lbl_dob=Label(self.root,text="dob:")
        lbl_dob.grid(row=2,column=0)
        ent_dob=Entry(self.root,textvariable=self.dob)
        ent_dob.grid(row=2,column=1)
        #gender
        lbl_gen=Label(self.root,text="gender:")
        lbl_gen.grid(row=3,column=0)
        com_gen = ttk.Combobox(self.root,textvariable = self.gen,state="readonly")
        com_gen['values'] = ('male',"female","other")
        com_gen.current(0)
        com_gen.grid(row = 3,column = 1)
        #submit button
        btn_submit=Button(self.root,text="submit",command=self.submitdata)
        btn_submit.grid(row=4,column=0)

    def dataStart(self):
            con = sqlite3.connect(r'C:\Users\sia\Documents\GitHub\student_management\data.db')
            cursor = con.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS stu_data(
                Name TEXT NOT NULL,
                roll TEXT NOT NULL,
                dob TEXT NOT NULL,
                gender TEXT NOT NULL
                )
            """)
            con.commit()
            con.close()

    def submitdata(self):
        con = sqlite3.connect(r'C:\Users\sia\Documents\GitHub\student_management\data.db')
        cursor = con.cursor()
        cursor.execute("INSERT INTO stu_data VALUES(?,?,?,?)",(self.name.get(),self.roll.get(),self.dob.get(),self.gen.get()))
        self.ent_name.delete(0,END)
        con.commit()
        con.close()


if __name__ == "__main__":
    root = Tk()
    l = login_window(root)
    root.mainloop()