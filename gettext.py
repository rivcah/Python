def gettext():
    global m
    username = m.get()
    suffix = '%ra'
    username = username[0:3]+suffix
    root0.destroy()
    print("A new user has been registered.\n The username is ",
          username.lower())
    
    
    

from tkinter import *
root0 = Tk()
root0.title("New User")
line1 = Label(root0, text = "Username")
line1.grid(row = 1, column = 1)
m = Entry(root0)
m.grid(row = 1, column = 2)
b1 = Button(root0, text = "send", command = gettext)
b1.grid(row = 2, column = 1)
