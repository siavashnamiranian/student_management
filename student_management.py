from tkinter import *
import tkinter.ttk as ttk
import sqlite3
from sqlite3 import Error
from tkinter import messagebox as ms

#windows
class login_window:
    def __init__(self,root):
        self.root=root
        self.create_login_table()
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
        login_btn = Button(root, text = 'log in', command = self.login)
        login_btn.grid(row=2,column=0)
        #register button
        register_btn = Button(root, text = 'register', command = self.register)
        register_btn.grid(row=2,column=1)

    #Login Function
    def login(self):
    	#Establish Connection
        with sqlite3.connect(r'C:\Users\sia\Documents\GitHub\student_management\data.db') as db:
            c = db.cursor()

        #Find user If there is any take proper action
        find_user = ('SELECT * FROM login_data WHERE username = ? and password = ?')
        c.execute(find_user,[(self.username_var.get()),(self.password.get())])
        result = c.fetchall()
        if result:
            
            root2 = Toplevel(self.root)
            enter = enter_data_window(root2)
        else:
            ms.showerror('Oops!','Username Not Found.')

    def register(self):
        	#Establish Connection
        with sqlite3.connect(r'C:\Users\sia\Documents\GitHub\student_management\data.db') as db:
            c = db.cursor()

        #Find Existing username if any take proper action
        find_user = ('SELECT username FROM login_data WHERE username = ?')
        c.execute(find_user,[(self.username_var.get())])        
        if c.fetchall():
            ms.showerror('Error!','duplicate username,try another.')
            
        #Create New Account 
        insert = ('INSERT INTO login_data(username,password) VALUES(?,?)')
        c.execute(insert,((self.username_var.get()),(self.password.get())))
        self.username_var.set('')
        self.password.set('')
        db.commit()
    def create_login_table(self):
            conn = sqlite3.connect(r'C:\Users\sia\Documents\GitHub\student_management\data.db')
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS login_data(
                username TEXT NOT NULL,
                password TEXT NOT NULL
                )
            """)
            conn.commit()
            conn.close()


    def secondScreen(self):
        root2 = Toplevel(self.root)
        enter = enter_data_window(root2)
class enter_data_window:
    def __init__(self,root):
        self.create_student_table()
        self.root = root
        self.root.geometry('300x150')
        self.root.title("enter data")
        self.name = StringVar()
        self.dob = StringVar()
        self.roll = StringVar()
        self.gen = StringVar()
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
        #show button
        btn_show=Button(self.root,text="show details",command=self.show_details)
        btn_show.grid(row=4,column=1)

    def create_student_table(self):
            conn = sqlite3.connect(r'C:\Users\sia\Documents\GitHub\student_management\data.db')
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS student_data(
                Name TEXT NOT NULL,
                roll TEXT NOT NULL,
                dob TEXT NOT NULL,
                gender TEXT NOT NULL
                )
            """)
            conn.commit()
            conn.close()

    def submitdata(self):
        conn = sqlite3.connect(r'C:\Users\sia\Documents\GitHub\student_management\data.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO student_data VALUES(?,?,?,?)",
        (self.name.get(),self.roll.get(),self.dob.get(),self.gen.get()))
        conn.commit()
        conn.close()
    def show_details(self):
        root3 = Toplevel(self.root)
        show = show_details_window(root3)

class show_details_window:
    def __init__(self,root):
        self.root = root
        self.root.state("zoomed")
        self.root.title("students viewer")
        #==========================tree
        tree=ttk.Treeview(self.root,column=("column1","column2","column3","column4"),show="headings")
        tree.heading("#1",text="name")
        tree.heading("#2",text="roll")
        tree.heading("#3",text="dob")
        tree.heading("#4",text="gender")
        conn = sqlite3.connect(r'C:\Users\sia\Documents\GitHub\student_management\data.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM student_data")
        rows = cur.fetchall()
        for row in rows:
            tree.insert("",END,values=row)
        conn.close()

        tree.pack()
        


if __name__ == "__main__":
    root = Tk()
    l = login_window(root)
    root.mainloop()