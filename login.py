from tkinter import *
from tkinter import messagebox
from functools import partial
import json
from tkinter import ttk
from tkinter.messagebox import showinfo

#login_details={"selcia":"project@123"}
class Stack:
    def __init__(self):
        self.st=[]
    def Push(self,k):
        self.st.append(k)
    def Pop(self):
        return self.st.pop()
    def top(self):
        if (len(self.st)):
            return self.st[-1]
        return 0

def goBack():
    global pages
    pages.top().withdraw()
    pages.Pop()
    pages.top().deiconify()
def admin_page():
    global pages
    with open("flat_details1.json", "r") as read_it:
            flat_details = json.load(read_it)

    window = Toplevel()
    window.geometry("1400x900")
    window.pack_propagate(True)
    window.title("Admin Page - Details of Occupants")
    window.resizable(height=None,width=None)
    pages.Push(window)

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

def tenant_page():
    window = Toplevel()
    window.geometry("1400x800")
    window.title("Occupant Payment Page")
    window.configure(bg="cornsilk2")
    Label(window,text="WELCOME TO GROUPOD HOUSING APARTMENTS", bg="dark turquoise", width="800", height="2", font=("Times", 32, "bold")).pack()
    Label(window,text="OCCUPANT PAYMENT PAGE", bg="black", fg="white",width="800", height="2", font=("Times", 28,"bold")).pack() 
    Label(window,text="",bg="cornsilk2").pack() 
    pages.Push(window)
    
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
    paymentButton=Button(window, text="Proceed to pay maintenance fee >>",command=Payment,font=("Times", 15,"bold"),bg="#0D47A1",fg="white").pack()
    window.mainloop()


def main_screen():
    global pages
    def read_saved_login_details():
        with open("login_details.json", "r") as read_it:
            login_details = json.load(read_it)
        return login_details

    def validate_login(username,password):
        username_entered = username.get()
        password_entered = password.get()
        login_details=read_saved_login_details()
        if username_entered in login_details:
            if login_details[username_entered] == password_entered:
                res = "LOGIN SUCCESSFUL"
            else:
                res = "INCORRECT PASSWORD"
        else:
            res = "INVALID USERNAME"
        messagebox.showinfo("LOGIN", res)

    def admin_login():
        global pages
        mainscreen1 = Toplevel(mainscreen)
        mainscreen1.geometry("1400x800") # set the configuration of GUI window 
        mainscreen1.title("Administrator Login Page") # set the title of GUI window
        mainscreen1.configure(bg="cornsilk2")
        pages.Push(mainscreen1)
        # create a Form label 
        Label(mainscreen1,text="WELCOME TO GROUPOD HOUSING APARTMENTS", bg="dark turquoise", width="800", height="2", font=("Times", 32, "bold")).pack()
        Label(mainscreen1,text="ADMINISTRATOR LOGIN PAGE", bg="black", fg="white",width="800", height="2", font=("Times", 28,"bold")).pack() 
        Label(mainscreen1,text="",bg="cornsilk2").pack()
        # create Login Button 
        usernameLabel = Label(mainscreen1, width="30",text="Username",bg="sky blue",font=("Times", 20,"bold")).pack()
        Label(mainscreen1,text="",bg="cornsilk2").pack()
        username = StringVar()
        usernameEntry = Entry(mainscreen1, width="34",textvariable=username,font=("Calibri", 20)).pack() 
        Label(mainscreen1,text="",bg="cornsilk2").pack()
        passwordLabel = Label(mainscreen1,width="30",text="Password",bg="sky blue",font=("Times", 20,"bold")).pack() 
        Label(mainscreen1,text="",bg="cornsilk2").pack() 
        password = StringVar()
        passwordEntry = Entry(mainscreen1, width="34",textvariable=password,font=("Calibri", 20), show='*').pack()
        Label(mainscreen1,text="",bg="cornsilk2").pack()

        # create a register button
        
        def validate_login3(username,password):
                username_entered = username.get()
                password_entered = password.get()
                login_details=read_saved_login_details()
                if username_entered in login_details:
                    if login_details[username_entered.lower()] == password_entered:
                        res = "LOGIN SUCCESSFUL"
                    else:
                        res = "INCORRECT PASSWORD"
                else:
                    res = "INVALID USERNAME"
                if res=="LOGIN SUCCESSFUL":
                    import admin_page
                    admin_page.display()
                else:
                    messagebox.showinfo("LOGIN", res)
        
        validateLogin = partial(validate_login3, username, password)
        loginButton = Button(mainscreen1, text="Login",font=("Times", 20,"bold"),bg="#0D47A1",fg="white",command=validateLogin).pack()
        Button(mainscreen1, text="Back",font=("Times", 20,"bold"),bg="#0D47A1",fg="white",command=goBack).pack()

        mainscreen1.mainloop() # start the GUI

    def tenant_login():
        global pages
        mainscreen2 = Toplevel(mainscreen)
        mainscreen2.geometry("1400x800") # set the configuration of GUI window 
        mainscreen2.title("Occupant Login Page") # set the title of GUI window
        mainscreen2.configure(bg="cornsilk2")
        pages.Push(mainscreen2)
        # create a Form label 
        Label(mainscreen2,text="WELCOME TO GROUPOD HOUSING APARTMENTS", bg="dark turquoise", width="800", height="2", font=("Times", 32, "bold")).pack()
        Label(mainscreen2,text="OCCUPANT LOGIN PAGE", bg="black", fg="white",width="800", height="2", font=("Times", 28,"bold")).pack() 
        Label(mainscreen2,text="",bg="cornsilk2").pack() 
        # create Login Button 
        usernameLabel = Label(mainscreen2, width="30",text="Username",bg="sky blue",font=("Times", 20,"bold")).pack()
        Label(mainscreen2,text="",bg="cornsilk2").pack()
        username = StringVar()
        usernameEntry = Entry(mainscreen2, width="34",textvariable=username,font=("Calibri", 20)).pack() 
        Label(mainscreen2,text="",bg="cornsilk2").pack()
        passwordLabel = Label(mainscreen2,width="30",text="Password",bg="sky blue",font=("Times", 20,"bold")).pack() 
        Label(mainscreen2,text="",bg="cornsilk2").pack() 
        password = StringVar()
        passwordEntry = Entry(mainscreen2, width="34",textvariable=password,font=("Calibri", 20), show='*').pack()
        Label(mainscreen2,text="",bg="cornsilk2").pack()
        # create a register button

        def validate_login2(username,password):
                username_entered = username.get()
                password_entered = password.get()
                login_details=read_saved_login_details()
                if username_entered in login_details:
                    if login_details[username_entered] == password_entered:
                        res = "LOGIN SUCCESSFUL"
                    else:
                        res = "INCORRECT PASSWORD"
                else:
                    res = "INVALID USERNAME"
                if res=="LOGIN SUCCESSFUL":
                    tenant_page()
                else:
                    messagebox.showinfo("LOGIN", res)

        validateLogin = partial(validate_login2, username, password)
        loginButton = Button(mainscreen2, text="Login", font=("Times", 20,"bold"),bg="#0D47A1",fg="white",command=validateLogin).pack()
        Button(mainscreen2, text="Back",font=("Times", 20,"bold"),bg="#0D47A1",fg="white",command=goBack).pack()

        mainscreen2.mainloop() # start the GUI
    
    def newuser_login():

        def newaccount_creation():

            def validate_password(password):
                num_count = 0
                char_count = 0
                for i in password:
                    if i.isdigit():
                        num_count += 1
                    if i in ["@", "+", "-", "_","."]:
                        char_count += 1
                return len(password) >= 8 and num_count >= 1 and char_count >= 1

            def validate_username(username):
                return len(username) >= 5 and len(username) <= 15

            def validate_user_creation(username, password, repassword):
                username1 = username.get()
                repassword1 = repassword.get()
                password1 = password.get()
                res = "Registration failed"
                login_details=read_saved_login_details()
                if password1 == repassword1:
                    if validate_password(password1):
                        if validate_username(username1):
                            if username1 not in login_details:
                                login_details[username1] = password1
                                res = "Registration successful"
                                with open("login_details.json", "w") as p:
                                    json.dump(login_details, p)
                            else:
                                res = "Username already exists!"
                        else:
                            res = "Invalid Username!"
                    else:
                        res = "Invalid Password!"
                else:
                    res = "Password not matching in both cases!"
                messagebox.showinfo("NEW ACCOUNT CREATION STATUS", res)

            mainscreen4 = Toplevel(mainscreen3)
            mainscreen4.geometry("1400x800") # set the configuration of GUI window 
            mainscreen4.title("New User Create Account Page") # set the title of GUI window
            mainscreen4.configure(bg="cornsilk2")
            # create a Form label 
            Label(mainscreen4,text="WELCOME TO GROUPOD HOUSING APARTMENTS", bg="dark turquoise", width="800", height="2", font=("Times", 32, "bold")).pack()
            Label(mainscreen4,text="NEW USER SIGNUP PAGE", bg="black", fg="white",width="800", height="2", font=("Times", 28,"bold")).pack() 
            Label(mainscreen4,text="",bg="cornsilk2").pack()
             
            Label(mainscreen4, text="REQUIRED*",fg="red",bg="cornsilk2",width="800", height="2", font=("Times", 15)).pack()
            Label(mainscreen4, text="Username should have atleast minimum 5 characters and maximum 15 characters*",bg="cornsilk2",fg="red",width="800", height="2", font=("Times", 13)).pack()
            Label(mainscreen4, text="Password should contain atleast minimum 8 characters with atleast 1 digit and 1 special character( @ , + , - , . , _ )*",bg="cornsilk2",fg="red",width="800", height="2", font=("Times", 13)).pack()
            # create Login Button
            usernameLabel = Label(mainscreen4, width="30",text="Username",bg="sky blue",font=("Times", 20,"bold")).pack()
            Label(mainscreen4,text="",bg="cornsilk2").pack()
            username = StringVar()
            usernameEntry = Entry(mainscreen4, width="34",textvariable=username,font=("Calibri", 20)).pack() 
            Label(mainscreen4,text="",bg="cornsilk2").pack()
            passwordLabel = Label(mainscreen4,width="30",text="Password",bg="sky blue",font=("Times", 20,"bold")).pack() 
            Label(mainscreen4,text="",bg="cornsilk2").pack() 
            password = StringVar()
            passwordEntry = Entry(mainscreen4, width="34",textvariable=password,font=("Calibri", 20), show='*').pack()
            Label(mainscreen4,text="",bg="cornsilk2").pack()
            repasswordLabel = Label(mainscreen4,width="30",text="Confirm password",bg="sky blue", font=("Times", 20,"bold")).pack() 
            Label(mainscreen4,text="",bg="cornsilk2").pack() 
            repassword = StringVar()
            repasswordEntry = Entry(mainscreen4, width="34",textvariable=repassword, font=("Calibri", 20),show='*').pack()
            Label(mainscreen4,text="",bg="cornsilk2").pack()
            # create a register button
            validateAccountCreation=partial(validate_user_creation,username, password, repassword)
            createAccountButton=Button(mainscreen4, text="Create Account",font=("Times", 20,"bold"),bg="#0D47A1",fg="white",command=validateAccountCreation).pack()
            mainscreen4.mainloop() 

        mainscreen3 = Toplevel(mainscreen)
        mainscreen3.geometry("1400x800") # set the configuration of GUI window 
        mainscreen3.title("New User Login Page") # set the title of GUI window
        mainscreen3.configure(bg="cornsilk2")
        # create a Form label 
        Label(mainscreen3,text="WELCOME TO GROUPOD HOUSING APARTMENTS", bg="dark turquoise", width="800", height="2", font=("Times", 32, "bold")).pack()
        Label(mainscreen3,text="NEW USER LOGIN PAGE", bg="black", fg="white",width="800", height="2", font=("Times", 28,"bold")).pack() 
        Label(mainscreen3,text="",bg="cornsilk2").pack()
        # create Login Button 
        usernameLabel = Label(mainscreen3, width="30",text="Username",bg="sky blue",font=("Times", 20,"bold")).pack()
        Label(mainscreen3,text="",bg="cornsilk2").pack()
        username = StringVar()
        usernameEntry = Entry(mainscreen3, width="34",textvariable=username,font=("Calibri", 20)).pack() 
        Label(mainscreen3,text="",bg="cornsilk2").pack()
        passwordLabel = Label(mainscreen3,width="30",text="Password",bg="sky blue",font=("Times", 20,"bold")).pack() 
        Label(mainscreen3,text="",bg="cornsilk2").pack() 
        password = StringVar()
        passwordEntry = Entry(mainscreen3, width="34",textvariable=password,font=("Calibri", 20), show='*').pack()
        Label(mainscreen3,text="",bg="cornsilk2").pack()

        def validate_login1(username,password):
                username_entered = username.get()
                password_entered = password.get()
                login_details=read_saved_login_details()
                if username_entered in login_details:
                    if login_details[username_entered] == password_entered:
                        res = "LOGIN SUCCESSFUL"
                    else:
                        res = "INCORRECT PASSWORD"
                else:
                    res = "INVALID USERNAME"
                
                if res=="LOGIN SUCCESSFUL":
                    import new_user
                    new_user.display_details()
                else:
                    messagebox.showinfo("LOGIN", res)

        validateLogin = partial(validate_login1, username, password)
        loginButton = Button(mainscreen3, text="Login",font=("Times", 20,"bold"),bg="#0D47A1",fg="white",command=validateLogin).pack()
        Label(mainscreen3,text="",bg="cornsilk2").pack()
        Label(mainscreen3,text="",bg="cornsilk2").pack()
        Label(mainscreen3,text="Not a member yet?",bg="pale turquoise",fg="black",width="32", height="2", font=("Times", 20)).pack()
        Label(mainscreen3,text="",bg="cornsilk2").pack()
        createAccountButton=Button(mainscreen3, text="Create Account",font=("Times", 20,"bold"),bg="#0D47A1",fg="white",command=newaccount_creation).pack()
        mainscreen3.mainloop() # start the GUI
 
    mainscreen = Tk()   # create a GUI window 
     
    mainscreen.geometry("1400x800") # set the configuration of GUI window 
    mainscreen.title("Login Page") # set the title of GUI window
    mainscreen.configure(bg="cornsilk2")
    # create a Form label 
    Label(text="WELCOME TO GROUPOD HOUSING APARTMENTS", bg="dark turquoise", width="800", height="2", font=("Times", 32, "bold")).pack() 
    Label(text="Please login to continue!", bg="black", fg="white", width="800", height="2", font=("Times", 30, "bold")).pack() 
    Label(text="",bg="cornsilk2").pack()
    Label(text="Login as Administator",bg="cornsilk2",width="800", height="2", font=("Times", 20)).pack()
    # create Login Button 
    Button(text="ADMIN", height="2", width="30",font=("Georgia", 20, "bold"),command=admin_login, ).pack() 
    Label(text="Login as a Member",bg="cornsilk2",width="800", height="2", font=("Times", 20)).pack()
    # create a register button
    Button(text="OCCUPANT", height="2",width="30",font=("Georgia", 20, "bold"),command=tenant_login).pack()
    Label(text="Haven't booked yet?",bg="cornsilk2",width="800", height="2", font=("Times", 20)).pack()
    Button(text="BOOK NOW", height="2",width="30",font=("Georgia", 20, "bold"),command=newuser_login).pack()
    Label(text="",bg="cornsilk2").pack() 
    mainscreen.mainloop() # start the GUI

pages=Stack()
main_screen()
