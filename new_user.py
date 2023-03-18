from tkinter import *
import json
from tkinter import messagebox
from functools import partial
from tkinter import ttk

def display_details():
    
    with open("flat_details1.json", "r") as read_it:
            flat_details = json.load(read_it)

    window = Toplevel()
    window.geometry("1410x900")
    window.pack_propagate(True)
    window.title("New User Page - List of Total Houses")
    window.resizable(height=None,width=None)

    #frame = LabelFrame(window, text="Total Houses")
    #frame.place(height=485, width=1170)

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

    treev["columns"] = ("1","2","3","4","5")

    treev['show'] = 'headings'

    treev.column("1", width = 90, anchor ='c')
    treev.column("2", width = 90, anchor ='c')
    treev.column("3", width = 90, anchor ='c')
    treev.column("4", width = 90, anchor ='c')
    treev.column("5", width = 90, anchor ='c')

    treev.heading("1", text ="BLOCK NO.")
    treev.heading("2", text ="FLAT NO.")
    treev.heading("3", text ="BHK TYPE")
    treev.heading("4", text ="OCCUPANCY")
    treev.heading("5", text ="PRICE")

    for i in flat_details:
        treev.insert("", 'end', text ="L1",tags="odd")
        treev.insert("", 'end', text ="L1",values =(i[1],i[2:],flat_details[i]["BHK"],flat_details[i]["Occupancy"],flat_details[i]["Price"]))
        treev.insert("", 'end', text ="L1",tags="odd")

    def flat_booking():
        def validate_booking(blockno,houseno,name,contact_no,aadharno,address):
            block_no=blockno.get()
            house_no=houseno.get()
            name_input=name.get()
            contactno=contact_no.get()
            aadhar_no=aadharno.get()
            address_input=address.get()
            res="Flat Booking Unsuccessful"
            if house_no in ["1","2","3","4","5","6","7","8","9"] and block_no in ["1","2","3"]:
                if house_no=="10":
                    house_booking="F"+block_no+house_no
                else:
                    house_booking="F"+block_no+"0"+house_no
                with open("flat_details1.json", "r") as read_it:
                    flat_details = json.load(read_it)
                    if flat_details[house_booking]["Occupancy"]=="Available":
                        res="Flat Booking Succesful\nContact Admin for Paymment and Further Details"
                        flat_details[house_booking]["Occupancy"]="Occupied"
                        flat_details[house_booking]["Name"]=name_input
                        flat_details[house_booking]["PhoneNumber"]=contactno
                        flat_details[house_booking]["AaadhaarNumber"]=aadhar_no
                        file1=open("new_bookings.txt","a")

                        file1.write(name_input+" "+contactno+" "+aadhar_no+" "+address_input+" "+block_no+" "+house_no+"\n")
                        file1.close()

                        with open("flat_details1.json", "w") as p:
                            json.dump(flat_details, p)
            messagebox.showinfo("Booking Status", res)

        window2 = Toplevel()
        window2.geometry("1410x900")
        window2.title("Flat Booking Page") 
        window2.configure(bg="cornsilk2")
    
        Label(window2,text="WELCOME TO GROUPOD HOUSING APARTMENTS", bg="dark turquoise", width="800", height="2", font=("Times", 32, "bold")).pack()
        Label(window2,text="NEW USER FLAT BOOKING PAGE", bg="black", fg="white",width="800", height="2", font=("Times", 28,"bold")).pack() 
        Label(window2,text="",bg="cornsilk2").pack() 

        nameLabel = Label(window2, width="35",text="Name",bg="sky blue", font=("Times", 17,"bold")).pack()
        
        name = StringVar()
        nameEntry = Entry(window2, width="41",textvariable=name, font=("Calibri", 17)).pack()
        Label(window2,text="",bg="cornsilk2").pack()

        contact_noLabel = Label(window2, width="35",text="Contact Number",bg="sky blue", font=("Times", 17,"bold")).pack()
        
        contact_no = StringVar()
        contact_noEntry = Entry(window2, width="41",textvariable=contact_no, font=("Calibri", 17)).pack()
        Label(window2,text="",bg="cornsilk2").pack()

        aadharLabel = Label(window2, width="35",text="Aadhaar Number",bg="sky blue", font=("Times", 17,"bold")).pack()
     
        aadharno = StringVar()
        aadharEntry = Entry(window2, width="41",textvariable=aadharno, font=("Calibri", 17)).pack() 
        Label(window2,text="",bg="cornsilk2").pack()

        addressLabel = Label(window2, width="35",text="Current Residential Address",bg="sky blue", font=("Times", 17,"bold")).pack()
        
        address = StringVar()
        addressEntry = Entry(window2, width="41",textvariable=address, font=("Calibri", 17)).pack() 
        Label(window2,text="",bg="cornsilk2").pack()

        blocknoEntry = Label(window2, width="35",text="Enter the block number you want to book",bg="sky blue",font=("Times", 17,"bold")).pack()
        
        blockno = StringVar()
        blocknoEntry = Entry(window2, width="41",textvariable=blockno, font=("Calibri", 17)).pack()
        Label(window2,text="",bg="cornsilk2").pack() 

        housenoLabel = Label(window2, width="35",text="Enter the flat number you want to book",bg="sky blue", font=("Times", 17,"bold")).pack()
        
        houseno = StringVar()
        HousenoEntry = Entry(window2, width="41",textvariable=houseno, font=("Calibri", 17)).pack()
        Label(window2,text="",bg="cornsilk2").pack()  

        booking = partial(validate_booking,blockno,houseno,name,contact_no,aadharno,address)
        bookingButton = Button(window2, text="Confirm booking flat",command=booking,font=("Times", 16,"bold"),bg="#0D47A1",fg="white").pack()
        window2.mainloop() 
    
    loginButton = Button(window, text="Book flat", command=flat_booking).pack()

    window.mainloop()


#display_details()