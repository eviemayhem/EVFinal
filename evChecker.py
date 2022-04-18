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

    maintList = ("Battery #5679", "Battery #3565")

    maint_var = tk.StringVar(value=maintList)

    
       
#---Creates new Window for Admin Dash ---#
    def openAdminDash():
        adminDash = Toplevel(root)
        adminDash.title("Admin Dashboard")
        adminDash.geometry("500x500")
        
        maintenanceLbl = Label(adminDash, text="Maintenance Logs")
        maintenanceLbl.pack()
        
        #create Listbox for Maintenance Logs
        maintLB= tk.Listbox(adminDash, listvariable=maint_var, height=5, selectmode='extended')
        maintLB.pack(pady=5)

        #---Event Handler for maintenance Listbox---#
        def batteryselect(event):
            print("Button clicked")

        #Get selected index
        selected_index = maintLB.curselection()
        #Get selected maintenance item
        selected_item = maintLB.get(selected_index)
        

#---Ask Admin to Login---#
    def buildLogin():
        #Variables 
        adminLbl = Label(root, text="Admin Username")
        admin = Text(root, height=1, width=20)
        passLbl = Label(root, text="Admin Password")
        passWord = Text(root, height=1, width=20) 
        
        #---Authenticate Admin---#     
        #Grab Admin textbox entry and username textbox entry
       
        def authenticate(): 
            if admin.get(1.0, "end-1c")=="admin" and passWord.get(1.0, "end-1c") =="admin":
                print("Authenticated")
                #Opens Admin Dashboard
                openAdminDash()
            else:
                print("Not Authenticated")
        #Button
        loginBtn = Button(root, text="Login", command=authenticate)
        #---Places Widgets---#
        adminLbl.pack()
        admin.pack()
        passLbl.pack()
        passWord.pack()
        loginBtn.pack()
       

    





    buildLogin()
    root.mainloop()
main()

