#Import tkinter modules
import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3

from matplotlib import pyplot as plt
import numpy as np
from numpy import append
import math
#These empties 
Impact_Detected_Int_list = []
Impact_Detected_Entry_list = []
Impact_Detected_DateTime_list = []
No_Impact_Detected_Int_list = []
No_Impact_Detected_Entry_list = []
No_Impact_Detected_DateTime_list = []
Temp_Int_list = []
Temp_Entry_list = []
Temp_Times = []
Invalid_Temp_Int_list = []
Invalid_Temp_Entry_list = []
Invalid_Temp_DateTime_list = []
# creating file path to connect to the dbfile, you will need to download sqlite pip in order to use this file
dbfile = 'c:/Users/yossa/Downloads/Valid_Temp_Range_Final_Project_1 (1).db'
        

# Create a SQL connection to our SQLite database
con = sqlite3.connect(dbfile)

# creating cursor
cur = con.cursor()


# reading all table names with the select sql command to copy all the records over from that table
table_view_Impact1 = [a for a in cur.execute("SELECT *  FROM 'Impact_Detected'")] 
table_view_Impact2 = [a for a in cur.execute("SELECT *  FROM 'No_Impact_Detected'")] 
table_view_Temperature1 = [a for a in cur.execute("SELECT * FROM 'Normal_Temp_Ranges'")] 
table_view_Temperature2 = [a for a in cur.execute("SELECT * FROM 'Invalid_Temp_Ranges'")] 
table_view_Mositure1 = [a for a in cur.execute("SELECT * FROM 'No_Moisture_Detected'")] 
table_view_Moisture2 = [a for a in cur.execute("SELECT * FROM 'Moisture_Detected'")] 
#This series of for loops will populate the different lists that will be used in the methods below for various reasons including generating graphs
for row in table_view_Mositure1 :
   Impact_Detected_Int_list.append(row[1])
   Impact_Detected_Entry_list.append(row[0])
   Impact_Detected_DateTime_list.append(row[2])
for row in table_view_Moisture2 :
   Impact_Detected_Int_list.append(row[1])
   Impact_Detected_Entry_list.append(row[0])
   Impact_Detected_DateTime_list.append(row[2])
for row in table_view_Impact1:
   Impact_Detected_Int_list.append(row[1])
   Impact_Detected_Entry_list.append(row[0])
   Impact_Detected_DateTime_list.append(row[2])
for row in table_view_Impact2:
   No_Impact_Detected_Int_list.append(row[1])
   No_Impact_Detected_Entry_list.append(row[0])
   No_Impact_Detected_DateTime_list.append(row[2])
for row in table_view_Temperature1:
   Temp_Int_list.append(row[1])
   Temp_Entry_list.append(row[0])
   Temp_Times.append(row[2])
for row in table_view_Temperature2:
   Invalid_Temp_Int_list.append((row[1]))
   Invalid_Temp_Entry_list.append(row[0])
   Invalid_Temp_DateTime_list.append(row[2])

#---Initializes Main Window---#

adminDash = Tk()
adminDash.title("Admin Dashboard")
adminDash.geometry("500x500")

#---Constants---#
maintList = ("Battery #5679", "Battery #3565")
maint_var = tk.StringVar(value=maintList)



#----Runs Maintenance Check---#
def runMaintCheck(i):
  #counter variables used to trigger the various windows: impact, moisture and temperature
    heat_check = 0
    cold_check = 0
    impact_check = 0
    water_check =  0   
    if i == 1:
          #checks the given test table to see if the cold or hot window is activated  
            for row in table_view_Temperature1:
                if row[1] > 80:
                    print ("This battery is too hot and requires maintenance")

                    heat_check += 1
                elif row[1] < 30:
                    print ("This battery is too cold and requires maintenance")
                    cold_check += 1
                else:
                    print("No maintance")
                 
                   
            for row in  table_view_Moisture2:
                if row[1] >= 1:
                    print("Moisture Detected")
                    water_check += 1

            if water_check > 0:
                waterWindow(i)         
            if heat_check > 0:
                heatWindow(i)
            elif heat_check <= 0:
                    plot1 = plt.subplot2grid((3, 3), (0, 0), colspan=2)
                    plot1.bar(Temp_Entry_list, Temp_Int_list)
                    plot1.set_title('Temperature Graph (Temps(F) over time(hr))')
                    plt.tight_layout()
                    plt.savefig("Environment1.jpg")

                    plt.show()
            elif cold_check > 0:
                coldWindow(i)
                plot1 = plt.subplot2grid((3, 3), (0, 0), colspan=2)
                plot1.bar(Temp_Entry_list, Temp_Int_list)
                plot1.set_title('Temperature Graph (Temps(F) over time(hr))')
                plt.tight_layout()
                plt.savefig("Environment1.jpg")

                plt.show()

            for row in table_view_Impact1:
                    if row[1] >= 137:
                        print("This battery suffered a serious impact")
                        impact_check += 1
                 
                        
                
            if impact_check > 0:
                plot3 = plt.subplot2grid((3, 3), (1, 0), rowspan=2)
                plot3.plot(Impact_Detected_Entry_list, Impact_Detected_Int_list)
                plot3.set_title('Impact Graph')

                plt.tight_layout()
                plt.savefig("Environment2.jpg")

                plt.show()
                impactWindow(i) 
            elif impact_check <= 0:
                plot3 = plt.subplot2grid((3, 3), (1, 0), rowspan=2)
                plot3.plot(No_Impact_Detected_Entry_list, No_Impact_Detected_Int_list)
                plot3.set_title('Impact Graph')
                plt.xlabel('Close this window when finished viewing', fontsize=20)
                plt.tight_layout()
                plt.savefig("Environment2.jpg")

                plt.show()
            

    elif i == 0:
            for row in  table_view_Mositure1:
                if row[1] >= 1:
                    print("Moisture Detected")
                    water_check += 1

            for row in table_view_Temperature2:
                if row[1] > 80:
                    print ("This battery is too hot and requires maintenance")
                    print(heat_check)
                    heat_check += 1

                elif row[1] < 30:
                    print ("This battery is too cold and requires maintenance")
                    print(cold_check)
                    cold_check += 1
                else:
                    print("No maintance")

            if water_check > 0:
                waterWindow(i) 
               
            if heat_check > 0:
                heatWindow(i)
            elif heat_check <= 0:
                plot1 = plt.subplot2grid((3, 3), (0, 0), colspan=2)
                plot1.bar(Temp_Entry_list, Temp_Int_list)
                plot1.set_title('Temperature Graph (Temps(F) over time(hr))')
                plt.xlabel('Close this window when finished viewing', fontsize=20)
                plt.tight_layout()
                plt.savefig("Environment.jpg")
            
                plt.show()
            elif cold_check > 0:
                plot1 = plt.subplot2grid((3, 3), (0, 0), colspan=2)
                plot1.bar(Invalid_Temp_Entry_list, Invalid_Temp_Int_list)
                plot1.set_title('Temperature Graph (Temps(F) over time(hr))')
                plt.xlabel('Close this window when finished viewing', fontsize=20)
                plt.tight_layout()
                plt.savefig("Environment.jpg")
                
                plt.show()
                coldWindow(i)
        
 
            for row in table_view_Impact2:
                if row[1] >= 137:
                    print("This battery suffered a serious impact")
     
                    impact_check += 1
                else:
                    print("No maintenance required")
                
            if impact_check > 0:
                plot3 = plt.subplot2grid((3, 3), (0, 0), colspan=2)
                plot3.plot(Impact_Detected_Entry_list, Impact_Detected_Int_list)
                plot3.set_title('Impact Graph (PSI over time(hr))')
                plt.xlabel('Close this window when finished viewing', fontsize=20)
                plt.tight_layout()
                plt.savefig("Environment.jpg")

                plt.show()
                impactWindow(i) 
            elif impact_check <= 0:
                plot3 = plt.subplot2grid((3, 3), (0, 0), colspan=2)
                plot3.plot(No_Impact_Detected_Entry_list, No_Impact_Detected_Int_list)
                plot3.set_title('Impact Graph (PSI over time(hr))')
                plt.xlabel('Close this window when finished viewing', fontsize=20)
                plt.tight_layout()
                plt.savefig("Environment.jpg")

                plt.show()
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
    
    

#----Create new GUI windows  for maintenance protocols---#
def heatWindow(i):
  
      
    mc = "false"
    protocolWindow = Toplevel(adminDash)
    protocolWindow.title("Maintenance Protocol")
    protocolWindow.geometry("500x500")

    maintLbl = Label(protocolWindow, text="OverHeating Protocol")
    maintLbl.pack(pady=10)

    protocolText = Label(protocolWindow, height=10, width=50, text = "Instruction for overheating maintenance protocol:\n1, Step 1: Seal the case. \nStep 2: Evacuate people from the area \nStep 3: Contact local fire department .")
    protocolText.pack(pady=10)
    maintComplete = Button(protocolWindow, text="Complete Maintenance", command=maintenanceComplete(i))
    maintComplete.pack(pady=10)
    
    
    


def coldWindow(i):
    protocolWindow = Toplevel(adminDash)
    protocolWindow.title("Maintenance Protocol")
    protocolWindow.geometry("500x500")

    maintLbl = Label(protocolWindow, text="Freezing Protocol")
    maintLbl.pack(pady=5)

    protocolText = Label(protocolWindow, height=10, width=50, text = "Instruction for freezing maintenance protocol:\nStep 1. Seal the case usign sealing feature\nStep 2. Activate teh artifical heating\nStep3. Repeat previous stages until temperature in optimal range.")
    protocolText.pack(pady=10)
    maintComplete = Button(protocolWindow, text="Complete Maintenance", command=maintenanceComplete(i))
    maintComplete.pack(pady=10)
    

def impactWindow(i):
    protocolWindow = Toplevel(adminDash)
    protocolWindow.title("Maintenance Protocol")


    protocolWindow.geometry("500x500")

    maintLbl = Label(protocolWindow, text="Impact Damage Protocol")
    maintLbl.pack(pady=5)

    protocolText = Label(protocolWindow, height=10, width=50, text = "Instruction for impact damage protocol: \nStep 1. Seal case using seal features\nStep 2. If the battery is leaking contact emergency authorities\nStep 3. If not leaking, return to fasility for inspection.")
    protocolText.pack(pady=10)
    maintComplete = Button(protocolWindow, text="Complete Maintenance", command=maintenanceComplete(i))
    maintComplete.pack(pady=10)

def waterWindow(i):
    protocolWindow = Toplevel(adminDash)
    protocolWindow.title("Maintenance Protocol")
    protocolWindow.geometry("500x500")

    maintLbl = Label(protocolWindow, text="Water Damage Protocol")
    maintLbl.pack(pady=5)

    protocolText = Label(protocolWindow, height=10, width=50, text = "Instruction for water damage protocol: \nStep 1. Activate case sealing feature\nStep 2. Activate water pumps to remove water\nStep 3. Recheck status and repeat steps if necissary.")
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

con.close()