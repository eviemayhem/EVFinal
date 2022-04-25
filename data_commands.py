import sqlite3

from matplotlib import pyplot as plt
from numpy import append
import Graphs
# creating file path
Int_list = []
Entry_list = []
dbfile = 'C:\Users\ilesh\EVFinal\Valid_Temp_Range_Final_Project_1 (2).db'

# Create a SQL connection to our SQLite database
Get_Methods_to_Temp = "SELECT method, Impact_Value FROM 'Impact_Detected' GROUP BY method;"

def get_methods_to_graph(connection):
    with connection:
        return con.exectute(Get_Methods_to_Temp).fetchall()
con = sqlite3.connect(dbfile)

# creating cursor
cur = con.cursor()

# reading all table names
#table_list = [a for a in cur.execute("INSERT INTO 'Impact_Detected'(Impact_Entry,Impact_Value, Impact_Time_Rec)VALUES(18 , 77, '2017-09-10') ")]
#con.commit()
table_view = [a for a in cur.execute("SELECT Impact_Entry,Impact_Value,Impact_Time_Rec  FROM 'Impact_Detected'")] 


for row in table_view:
   print ("Entry = ", row[0])
   Int_list.append(row[1])
   Entry_list.append(row[0])
   print ("Value = ", row[1])
   print ("Date = ", row[2])
   if row[1] > 86:
       print("impact too high")
# here is you table list
#table_view = [a for a in cur.execute("SELECT Impact_Value FROM 'Impact_Detected' WHERE Impact_Entry = 8")]

#Graphs.method_temp_range_bar(Get_Methods_to_Temp)

plt.plot(Entry_list, Int_list)

plt.show()
# Be sure to close the connection


con.close()
 