from typing import final


# Software Analysis final

#Import tkinter modules
from tkinter import *
from tkinter import ttk

#---Initializes Main Window---#
def main():
    root = Tk()
    root.title("EV Checker")
    root.geometry("500x500")


#---Ask Admin to Login---#
    def buildLogin():
        
        #---Authenticate Admin---#        
        def authenticate():
            if admin=="admin" and passWord =="admin":
                print("Authenticated")
            else:
                print("Not Authenticated")

        adminLbl = Label(root, text="Admin Username")
        admin = Text(root, height=1, width=20)
        passLbl = Label(root, text="Admin Password")
        passWord = Text(root, height=1, width=20)
        loginBtn = Button(root, text="Login", command=authenticate)
        adminLbl.pack()
        admin.pack()
        passLbl.pack()
        passWord.pack()
        loginBtn.pack()
        





    buildLogin()
    root.mainloop()
main()

