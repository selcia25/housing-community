# housing-community
A system to manage the occupancy of a housing community

This system has three login modules where-in each module has a different functionality.
1.	ADMINISTRATOR MODULE 
In this module, the administrator will be able to login and manage the whole system in an effective and efficient manner.
2.	OCCUPANT MODULE 
In this module the occupants who’ve already bought the house & are residing in it will be able to login and pay their monthly maintenance fee.
3.	NEW USER MODULE
In this module the user can create an account if he doesn’t have one and allows him to login if he’s an existing user.

Implementation of Admin Module :

•	Here’s a list of block wise list of flat numbers with the occupant details, flat number, block number, name, mobile number and state of occupancy.
•	Once the system administrator logins, he’ll be able to view the details as mentioned above.
•	He can view the details of the occupants’ payment status as well.
•	Thus, the system can generate a block wise list of occupant details which will make it easy for the administrator to manage the housing community.
•	With JSON files as a backend to store data and Python’s Tkinter as the frontend this module was developed.
•	First, we validate the admin’s login and allow the administrator to view the client details
•	Here we’ve used tkinter’s module named Treeview tkinter to establish a table with all the required content.
•	Also, the admin can let an occupant vacate by clicking on “Delete”

Implementation of Occupant Module :

•	Once the system occupant logins, he’ll be asked to give his block number and flat number.
•	If the entered flat number and block number is correct then the payment portal will be opened.
•	Then the occupant will be asked to select the payment option to proceed further.
•	The payment will be successful when the occupant clicks the “Click To Pay” button.

Implementation of New User Module :

•	The new user will be able to either login and see the flat details or book a house if he already has an account.
•	If he doesn’t have the account, he will be able to create a new account
•	He can view the details of the flat details, along with BHK type and price of each house depending on the type of BHK
•	Thus, the system can generate a block wise list of flat details which will make it easy for the occupant to book a flat.
•	With Python as a backend and Tkinter as the frontend this module was developed.
•	First, we validate the new user’s login and allow the new user to view the flat details in order to book a house
•	If he doesn’t have an account, he’ll be asked to create an account based on the rules displayed on the screen 
•	Then the user will be asked to enter his details like phone number, aadhaar number, name, flat number, block number in order to book a new flat.
•	Here we’ve used tkinter’s module named Treeview tkinter to establish a table with all the required content


DATA STRUCTURES USED 

1.	Dictionary -
We have used dictionary to store details of flat, occupants, etc. in the form of a json file.
 
2.	Stack -
•	We have used stack to implement opening of windows in a easier way of just pressing the “Go back” button

   
