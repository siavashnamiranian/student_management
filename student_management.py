from tkinter import *

#windows
root = Tk()
root.title("student management")
root.geometry("250x100")

#user name label and entry
usernamelabel_var=StringVar()
label = Label( root, textvariable=usernamelabel_var, relief=RAISED )
usernamelabel_var.set("user name:")

usernameentry_var=StringVar()
entry=Entry(root,textvariable=usernameentry_var)

label.grid(row=0,column=0)
entry.grid(row=0,column=1)

#password label and entry
pass_var=StringVar()
label_pass = Label( root, textvariable=pass_var, relief=RAISED )
pass_var.set("password:")

entry_var=StringVar()
entry_pass=Entry(root,textvariable=entry_var,show="*")

label_pass.grid(row=1,column=0)
entry_pass.grid(row=1,column=1)
#login button
login_btn = Button(root, text = 'log in', bd = '5', command = root.destroy)
login_btn.grid(row=2,column=0)
#register button
register_btn = Button(root, text = 'register', bd = '5', command = root.destroy)
register_btn.grid(row=2,column=1)
root.mainloop()
