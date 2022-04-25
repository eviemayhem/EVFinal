from typing import final


# Software Analysis final

#Import tkinter modules
import tkinter as tk
from tkinter import *
from tkinter import ttk

#---Initializes Main Window---#
def main():
    root = Tk()
    root.title("EV Checker")
    root.geometry("500x500")

#---Constant Variables---#


    
#---Ask Admin to Login---#
    def buildLogin():
        #Variables 
        textlbl = Label(root, text="Please enter your username and password")
        adminLbl = Label(root, text="Admin Username")
        admin = Text(root, height=1, width=20)
        textlbl.pack(pady=5)
        passLbl = Label(root, text="Admin Password")
        passWord = Text(root, height=1, width=20) 
        
        #---Authenticate Admin---#     
        #Grab Admin textbox entry and username textbox entry
       
        def authenticate(): 
            if admin.get(1.0, "end-1c")=="admin" and passWord.get(1.0, "end-1c") =="admin":
                print("Authenticated")
                #Opens Admin Dashboard
                root.destroy()
                import adminDashboard
            else:
                textlbl.config(text="Invalid Username or Password")
        #Button
        loginBtn = Button(root, text="Login", command=authenticate)
        #---Places Widgets---#
        adminLbl.pack(pady=5)
        admin.pack(pady=5)
        passLbl.pack(pady=5)
        passWord.pack(pady=5)
        loginBtn.pack(pady=5)
       

    





    buildLogin()
    root.mainloop()
main()

