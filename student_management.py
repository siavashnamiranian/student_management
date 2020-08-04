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
        enter = enter_data_window(root2)
class enter_data_window:
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
        #show button
        btn_show=Button(self.root,text="show details",command=self.show_details)
        btn_show.grid(row=4,column=1)

    def dataStart(self):
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
        cursor.execute("INSERT INTO student_data VALUES(?,?,?,?)",(self.name.get(),self.roll.get(),self.dob.get(),self.gen.get()))
        conn.commit()
        conn.close()
    def show_details(self):
        root3 = Toplevel(self.root)
        show = show_details_window(root3)

class show_details_window:
    def __init__(self,root):
        self.root = root
        self.root.geometry('800x500')
        self.root.title("students viewer")
        #==========================Show Frame
        show_frame = Frame(self.root,bg = "#B402FE")
        show_frame.place(width = 800,x = 0,y = 0 ,height = 50)
        labl_show = Label(show_frame,bg = "#B402FE",fg = "white",font = ("lucida",25,"bold"),text = "Details of Students")
        labl_show.pack()
        #========================Main Frame
        main_frame = Frame(self.root,bd = 10,relief = SUNKEN)
        main_frame.place(width = 780,height = 430,x = 8,y = 58)
        tree = ttk.Treeview(main_frame,height = 200)
        tree['columns'] = ("Name","Roll No","D-O-B","Gender")
        tree.column('#0',width=50,minwidth = 25)
        tree.column('Name',width=50,minwidth = 25)
        tree.column('Roll No',width=50,minwidth = 25)
        tree.column('D-O-B',width=50,minwidth = 25)
        tree.column('Gender',width=50,minwidth = 25)
        tree.heading("#0",text = "ID",anchor = W)
        tree.heading("Name",text = "Name",anchor = W)
        tree.heading("Roll No",text = "Roll No",anchor = W)
        tree.heading("D-O-B",text = "D-O-B",anchor = W)
        tree.heading("Gender",text="Gender",anchor = W)
        con = sq.connect('data.db')
        cursor = con.cursor()
        cursor.execute("SELECT * FROM stu_data")
        result = cursor.fetchall()
        for i in result:
            tree.insert("","end",text = f"{i[0]}",values = (f'{i[1]}',f'{i[2]}',f'{i[3]}',f'{i[4]}'))
        vsb = ttk.Scrollbar(main_frame,command = tree.yview,orient = "vertical")
        tree.configure(yscroll = vsb.set)
        vsb.pack(side = RIGHT,fill = Y)
        tree.pack(side = TOP,fill = X)


if __name__ == "__main__":
    root = Tk()
    l = login_window(root)
    root.mainloop()