#Import tkinter modules
import tkinter as tk
from tkinter import *
from tkinter import ttk

#---Initializes Main Window---#

adminDash = Tk()
adminDash.title("Admin Dashboard")
adminDash.geometry("500x500")

#---Constants---#
maintList = ("Battery #5679", "Battery #3565")
maint_var = tk.StringVar(value=maintList)

battListTemp = [99.6, 22.8]


#----Runs Maintenance Check---#
def runMaintCheck(i):
    if battListTemp[i] > 80:
        print ("This battery is too hot and requires maintenance")
        heatWindow(i)
    elif battListTemp[i] < 30:
        print ("This battery is too cold and requires maintenance")
        coldWindow(i)
    else:
        print("No maintenance required")

#---Grabs Battery Selection and determines which menu to pull up---#
def batterySelect():
    print ("Button Pressed")
    maintLog = maintLB.curselection()
    print (maintLog)
    #find value of selected item
    if maintLog == (0,):
        print("Battery #5679")
        i =0
        runMaintCheck(i)
    elif maintLog == (1,):
        i=1
        print("Battery #3565")
        runMaintCheck(i)
    else:
        print("Invalid Entry")
        
#----Removes the item from Maintenance List and from battListTemp---#
def maintenanceComplete(i):
    print("Maintenance Complete")
    maintLB.delete(i, )
    battListTemp.pop(i)
    print(battListTemp)
    
    
    
    

    

#----Create new GUI windows  for maintenance protocols---#
def heatWindow(i):
    
    mc = "false"
    protocolWindow = Toplevel(adminDash)
    protocolWindow.title("Maintenance Protocol")
    protocolWindow.geometry("500x500")

    maintLbl = Label(protocolWindow, text="OverHeating Protocol")
    maintLbl.pack(pady=10)

    protocolText = Label(protocolWindow, height=10, width=50, text = "Instruction for overheating maintenance protocol should go here.")
    protocolText.pack(pady=10)
    maintComplete = Button(protocolWindow, text="Complete Maintenance", command=maintenanceComplete(i))
    maintComplete.pack(pady=10)
    
    
    


def coldWindow(i):
    protocolWindow = Toplevel(adminDash)
    protocolWindow.title("Maintenance Protocol")
    protocolWindow.geometry("500x500")

    maintLbl = Label(protocolWindow, text="Freezing Protocol")
    maintLbl.pack(pady=5)

    protocolText = Label(protocolWindow, height=10, width=50, text = "Instruction for freezing maintenance protocol should go here.")
    protocolText.pack(pady=10)
    maintComplete = Button(protocolWindow, text="Complete Maintenance", command=maintenanceComplete(i))
    maintComplete.pack(pady=10)
    

def impactWindow(i):
    protocolWindow = Toplevel(adminDash)
    protocolWindow.title("Maintenance Protocol")
    protocolWindow.geometry("500x500")

    maintLbl = Label(protocolWindow, text="Impact Damage Protocol")
    maintLbl.pack(pady=5)

    protocolText = Label(protocolWindow, height=10, width=50, text = "Instruction for impact damage protocol should go here.")
    protocolText.pack(pady=10)
    maintComplete = Button(protocolWindow, text="Complete Maintenance", command=maintenanceComplete(i))
    maintComplete.pack(pady=10)

def waterWindow(i):
    protocolWindow = Toplevel(adminDash)
    protocolWindow.title("Maintenance Protocol")
    protocolWindow.geometry("500x500")

    maintLbl = Label(protocolWindow, text="Water Damage Protocol")
    maintLbl.pack(pady=5)

    protocolText = Label(protocolWindow, height=10, width=50, text = "Instruction for water damage protocol should go here.")
    protocolText.pack(pady=10)
    maintComplete = Button(protocolWindow, text="Complete Maintenance", command=maintenanceComplete(i))
    maintComplete.pack(pady=10)
    



        
maintenanceLbl = Label(adminDash, text="Maintenance Logs")
maintenanceLbl.pack()
        
#create Listbox for Maintenance Logs
maintLB= tk.Listbox(adminDash, listvariable=maint_var, height=5, selectmode='single')
maintLB.pack(pady=5)


maintBtn = tk.Button(adminDash, text="View Maintenance Log", command = batterySelect)
maintBtn.pack(pady=5)












adminDash.mainloop()

