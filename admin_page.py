from tkinter import *
import json
from tkinter import messagebox
from functools import partial
from tkinter import ttk

def display():

    with open("flat_details1.json", "r") as read_it:
            flat_details = json.load(read_it)

    window = Toplevel()
    window.geometry("1400x900")
    window.pack_propagate(True)
    window.title("Admin Page - Details of Occupants")
    window.resizable(height=None,width=None)
     

    #frame = LabelFrame(window, text="Occupancy & Details of Occupants",labelanchor="n",font=("Times", 20,"bold"),background="black",foreground="white")
    #frame.place(height=900, width=1400)

    style = ttk.Style()
    style.theme_use('clam')
    style.configure("mystyle.Treeview", font=("Times", 11))
    style.map("Treeview")
    style.configure("mystyle.Treeview.Heading", font=("Times", 13, "bold"))

    treev = ttk.Treeview(window, style="mystyle.Treeview")
    treev.place(relheight=1, relwidth=1)

    treescrolly = ttk.Scrollbar(window, orient="vertical", command=treev.yview)
    treescrollx = ttk.Scrollbar(window, orient="horizontal", command=treev.xview)
    treev.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
    treescrollx.pack(side="bottom", fill="x")
    treescrolly.pack(side="right", fill="y")

    treev["columns"] = ("1","2","3","4","5","6")

    treev['show'] = 'headings'
    
    treev.column("1", width = 3, anchor ='c')
    treev.column("2", width = 10, anchor ='c')
    treev.column("3", width = 90, anchor ='c')
    treev.column("4", width = 45, anchor ='c')
    treev.column("5", width = 90, anchor ='c')
    treev.column("6", width = 220, anchor ="c")

    treev.heading("1", text ="BLOCK NO.")
    treev.heading("2", text ="FLAT NO.")
    treev.heading("3", text ="NAME OF THE OCCUPANT")
    treev.heading("4", text ="CONTACT NO.")
    treev.heading("5", text ="AADHAAR NO.")
    treev.heading("6", text="MONTHLY MAINTENANCE FEE STATUS")

    file1=open("monthly_maintenance.txt","r")
    text=file1.read().split()
    houses_paid=[]
    for house in text[::2]:
        houses_paid.append(house)
    treev.insert("", 'end', text ="L1",tags="odd")

    for i in flat_details:
        house_no=i[2:]
        block_no=i[1]
        if house_no=="10":
            house_check="F"+block_no+house_no
        else:
            house_check="F"+block_no+house_no
        if flat_details[i]["Occupancy"] =="Occupied":
            if house_check in houses_paid:
                res="Paid"
            else:
                res="Not Paid Yet"
        else:
            res="Not Occupied"
        treev.insert("", 'end', text ="L1",tags="odd")
        treev.insert("", 'end', text ="L1",values =(block_no,house_no,flat_details[i]["Name"],str(flat_details[i]["PhoneNumber"]),str(flat_details[i]["AaadhaarNumber"]),res),tags="odd")
        treev.insert("", 'end', text ="L1",tags="odd")
    
    treev.insert("", 'end', text ="L1",tags="odd")

    treev.tag_configure('odd', background='sky blue', font=("Times", 15))

    window.mainloop()
#display()