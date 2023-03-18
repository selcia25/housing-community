from tkinter import *
import json
from tkinter import messagebox
from functools import partial
from tkinter import ttk
from tkinter.messagebox import showinfo
def display():
    window = Toplevel()
    window.geometry("1400x800")
    window.title("Occupant Payment Page")
    window.configure(bg="cornsilk2")
    Label(window,text="WELCOME TO GROUPOD HOUSING APARTMENTS", bg="dark turquoise", width="800", height="2", font=("Times", 32, "bold")).pack()
    Label(window,text="OCCUPANT PAYMENT PAGE", bg="black", fg="white",width="800", height="2", font=("Times", 28,"bold")).pack() 
    Label(window,text="",bg="cornsilk2").pack() 
    
    blocknoLabel = Label(window, width="30",text="Enter your Block Number",bg="sky blue",font=("Times", 20,"bold")).pack()
    Label(window,text="",bg="cornsilk2").pack()
    blockno = StringVar()
    blockEntry = Entry(window, width="34",textvariable=blockno,font=("Calibri", 20)).pack()
    Label(window,text="",bg="cornsilk2").pack()
    housenoLabel = Label(window, width="30",text="Enter your House Number",bg="sky blue",font=("Times", 20,"bold")).pack()
    Label(window,text="",bg="cornsilk2").pack()
    houseno = StringVar()
    housenoEntry = Entry(window, width="34",textvariable=houseno,font=("Calibri", 20)).pack() 
    Label(window,text="",bg="cornsilk2").pack()
    
    def payment(houseno,blockno):
        block_no=blockno.get()
        house_no=houseno.get()
        if house_no=="10":
            house_check="F"+block_no+house_no
        else:
            house_check="F"+block_no+"0"+house_no
        file1=open("monthly_maintenance.txt","r")
        text=file1.read().split()
        house_numbers_paid=[]
        for i in range(0,len(text),2):
            house_numbers_paid.append(text[i])
        
        with open("flat_details1.json", "r") as read_it:
            flat_details = json.load(read_it)
        if house_check in house_numbers_paid:
            res="You've already paid your maintenance fees!"
            messagebox.showinfo("MAINTENANCE FEES PAYMENT", res)
        elif flat_details[house_check]["Occupancy"] == "Available":
            res="Payment not Possible\n Flat is vacant"
            messagebox.showinfo("MAINTENANCE FEES PAYMENT", res)
        else:
            window1=Toplevel()
            window1.geometry("1400x800")
            window1.title("Occupant Payment Portal")
            window.configure(bg="cornsilk2")
            window1.configure(bg="cornsilk2")
            Label(window1,text="WELCOME TO GROUPOD HOUSING APARTMENTS", bg="dark turquoise", width="800", height="2", font=("Times", 32, "bold")).pack()
            Label(window1,text="OCCUPANT PAYMENT PORTAL", bg="black", fg="white",width="800", height="2", font=("Times", 28,"bold")).pack() 
            Label(window1,text="",bg="cornsilk2").pack() 
            Label(window1, text="Please select a payment method*",fg="red",bg="cornsilk2",width="800", height="2", font=("Times", 15)).pack()
            Label(window1,text="",bg="cornsilk2").pack()
            window1.resizable(height=0,width=0)
            def show_selected():
                showinfo(title='Result',message=selected_type.get())
            selected_type = StringVar()
            
            cash="Rs.1000" #same value for all apartments
            sizes = (('UPI', f'Payment of {cash} successful'),
                    ('Net banking', f'Payment of {cash} successful'))

            for size in sizes:
                r = ttk.Radiobutton(window1,text=size[0],value=size[1],variable=selected_type)
                r.pack(fill='x',padx=550, pady=10, side=TOP)

            style= ttk.Style(window1)
            style.configure("TRadiobutton", background = "snow2", foreground = "black", font = ("Times", 20, "bold"))
            Label(window1,text="",bg="cornsilk2").pack()
            Label(window1,text="",bg="cornsilk2").pack()
            Label(window1,text="",bg="cornsilk2").pack()
            Label(window1,text="",bg="cornsilk2").pack()
            Label(window1,text="TOTAL MAINTENANCE FEE : Rs.1000.00",bg="cornsilk2",font = ("Times", 15, "bold")).pack()
            Label(window1,text="",bg="cornsilk2").pack()
            button = Button(window1,text="CLICK TO PAY",command=show_selected,font=("Times", 15,"bold"),bg="#0D47A1",fg="white")
            button.pack(padx=5, pady=5)
          
            window1.mainloop()
            file1=open("monthly_maintenance.txt","a")
            from datetime import date
            today = date.today()
            file1.write(house_check+" "+str(today)+"\n")
            file1.close()

    Payment=partial(payment,houseno,blockno)  
    paymentButton=Button(window, text="Proceed to pay maintanance fee >>",command=Payment,font=("Times", 15,"bold"),bg="#0D47A1",fg="white").pack()
    button = Button(window,text="CLICK To leave",font=("Times", 15,"bold"),bg="#0D47A1",fg="white")
    button.pack(padx=10, pady=10)
    window.mainloop()
#display()