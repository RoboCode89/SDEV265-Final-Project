from tkinter import *
from tkinter import messagebox
from newlogin import *
from FoodMenu import *
from Reservations import *
from Menu import *

TK = Tk()

# Providing Settings for Window
TK.title("Restaurant POS")

wHeight = 400
wWidth = 700

sHeight = TK.winfo_screenheight()
sWidth = TK.winfo_screenwidth()

x = (sWidth / 2) - (wWidth / 2)
y = (sHeight / 2) - (wHeight / 2)

TK.geometry(f'{wWidth}x{wHeight}+{int(x)}+{int(y)}')

# Creating Frames

frameLogin = Frame(TK, width=wWidth, height=wHeight, padx=wWidth/2.9, pady=wHeight/7, bg="black")
frameMain = Frame(TK, width=wWidth, height=wHeight, padx=wWidth/2.45, pady=wHeight/5, bg="black")
frameHost = Frame(TK, width=wWidth, height=wHeight, padx=wWidth/2.5, pady=wHeight/5, bg="black")
frameReservation = Frame(TK, width=wWidth, height=wHeight, padx=wWidth/3.5, pady=wHeight/5, bg="black")
frameServer = Frame(TK, width=wWidth, height=wHeight, padx=wWidth/2.7, pady=wHeight/8, bg="black")
frameAppetizer = Frame(TK, width=wWidth, height=wHeight, padx=wWidth/3.2, pady=wHeight/5, bg="black")
frameEntree = Frame(TK, width=wWidth, height=wHeight, padx=wWidth/4, pady=wHeight/5, bg="black")
frameDessert = Frame(TK, width=wWidth, height=wHeight, padx=wWidth/3.2, pady=wHeight/5, bg="black")
frameDrink = Frame(TK, width=wWidth, height=wHeight, padx=wWidth/2.9, pady=wHeight/5, bg="black")
frameAlcohol = Frame(TK, width=wWidth, height=wHeight, padx=wWidth/3.2, pady=wHeight/5, bg="black")
frameLogin.pack(fill="both", expand=1)

# Creating an entry box for the pin

entry = Entry(frameLogin, width=30, borderwidth=5)

# Defining Activity Functions

# Inputs a number into the entry box for the pin
def buttonNum(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current)+str(number))

# A series of statements to determine the range of the given pin and perform the appropriate action
def enter():
    current = entry.get()
    if int(current)<1000 or int(current)>9999:
        clear()
        popup1()
    elif int(current)>=1000 and int(current)<2000:
        button_m1["state"] = ACTIVE
        button_m2["state"] = ACTIVE
        clear()
        close_menus()
        main_menu()
    elif int(current)>=2000 and int(current)<3000:
        button_m1["state"] = DISABLED
        button_m2["state"] = ACTIVE
        clear()
        close_menus()
        main_menu()
    elif int(current)>=3000 and int(current)<4000:
        button_m1["state"] = ACTIVE
        button_m2["state"] = DISABLED
        clear()
        close_menus()
        main_menu()
    elif int(current)>3999:
        clear()
        popup2()

# A warning popup window for if the given pin isn't 4 digits
def popup1():
    messagebox.showerror("Error", "Enter a 4 digit pin to proceed")

# A warning popup window for if the given pin is outside the range for employees
def popup2():
    messagebox.showerror("Invalid", "The given Pin is outside the available range for employees")

# Simply clears the entry field for a new pin attempt
def clear():
    entry.delete(0, END)

# Adds price to the bill, appends the appetizer list, and asks if the guest wants bread
def appButton(number):
    global bill
    bill += appList[number].getPrice()
    res = messagebox.askquestion("Additions", "Add Bread?")
    if res == "yes":
        bill += 1.00
        setAddBread = True
    else:
        setAddBread = False
    appToAddList.append(Appetizer(appList[number].getName(), appList[number].getPrice(), setAddBread))
    if setAddBread == True:
        appToAddList.append("Added Bread 1.00")

# Adds price to the bill, appends the entree list, and asks if the guest wants soup or salad
def entreeButton(number):
    global bill
    bill += entreeList[number].getPrice()
    res = messagebox.askquestion("Additions", "Add Soup?")
    if res == "yes":
        bill += 2.00
        setAddSoup = True
    else:
        setAddSoup = False
    res = messagebox.askquestion("Additions", "Add Salad?")
    if res == "yes":
        bill += 2.00
        setAddSalad = True
    else:
        setAddSalad = False
    entreeToAddList.append(Entree(entreeList[number].getName(), entreeList[number].getPrice(), setAddSoup, setAddSalad))
    if setAddSoup == True:
        entreeToAddList.append("Added Soup $2.00")
    if setAddSalad == True:
        entreeToAddList.append("Added Salad $2.00")

# Adds price to the bill, appends the dessert list, and asks if the guest wants the dessert to be a la mode
def desButton(number):
    global bill
    bill += dessertList[number].getPrice()
    res = messagebox.askquestion("Additions", "Make dessert a la mode?")
    if res == "yes":
        bill += 2.00
        setAddAlaMode = True
    else:
        setAddAlaMode = False
    dessertToAddList.append(Dessert(dessertList[number].getName(), dessertList[number].getPrice(), setAddAlaMode))
    if setAddAlaMode == True:
        dessertToAddList.append("Dessert Made A La Mode $2.00")

# Adds price to the bill, appends the drink list, and asks if the guest wants a lemon or sugar added to their drink
def drinkButton(number):
    global bill
    bill += drinkList[number].getPrice()
    res = messagebox.askquestion("Additions", "Add Lemon?")
    if res == "yes":
        setAddLemon = True
    else:
        setAddLemon = False
    res = messagebox.askquestion("Additions", "Add Sugar?")
    if res == "yes":
        setAddSugar = True
    else:
        setAddSugar = False
    drinkToAddList.append(Drink(drinkList[number].getName(), drinkList[number].getPrice(), setAddLemon, setAddSugar))
    if setAddLemon == True:
        drinkToAddList.append("Lemon Added")
    if setAddSugar == True:
        drinkToAddList.append("Sugar Added")

# Adds price to the bill, appends the alcohol list, and asks if the guest wants whipped cream or a doubleshot added to their drink
def alcButton(number):
    global bill
    bill += alcoholList[number].getPrice()
    res = messagebox.askquestion("Additions", "Add Whipped Cream?")
    if res == "yes":
        setAddWhippedCream = True
    else:
        setAddWhippedCream = False
    res = messagebox.askquestion("Additions", "Add Doubleshot?")
    if res == "yes":
        bill += 3.00
        setAddDoubleshot = True
    else:
        setAddDoubleshot = False
    alcoholToAddList.append(Alcohol(alcoholList[number].getName(), alcoholList[number].getPrice(), setAddWhippedCream, setAddDoubleshot))
    if setAddWhippedCream == True:
        alcoholToAddList.append("Whipped Cream Added")
    if setAddDoubleshot == True:
        alcoholToAddList.append("Added Doubleshot $3.00")

# Appends the items inside the various lists to the final order, outputs the final bill alongside a list of the various items and
# their prices, and then empties all the lists and sets bill to 0 for the next order
def placeOrder():
    global bill
    global billList
    global appToAddList
    global entreeToAddList
    global dessertToAddList
    global drinkToAddList
    global alcoholToAddList
    count = 0
    if(len(appToAddList) > 0):
        while(count < len(appToAddList)):
            billList.append(appToAddList[count])
            count += 1
    count = 0
    if(len(entreeToAddList) > 0):
        while(count < len(entreeToAddList)):
            billList.append(entreeToAddList[count])
            count += 1
    count = 0
    if(len(dessertToAddList) > 0):
        while(count < len(dessertToAddList)):
            billList.append(dessertToAddList[count])
            count += 1
    count = 0
    if(len(drinkToAddList) > 0):
        while(count < len(drinkToAddList)):
            billList.append(drinkToAddList[count])
            count += 1
    count = 0
    if(len(alcoholToAddList) > 0):
        while(count < len(alcoholToAddList)):
            billList.append(alcoholToAddList[count])
            count += 1
    messagebox.showinfo("Total Bill", "$%.2f" % (bill))
    messagebox.showinfo("Complete Order", billList)
    for i in billList:
        print(i)
    bill = 0.00
    billList = []
    appToAddList = []
    entreeToAddList = []
    dessertToAddList = []
    drinkToAddList = []
    alcoholToAddList = []

# Doesn't function, but would have added guests to the reservation list via a function inside of another file
def addReservation():
    Reservation.add_guest_reservation()

# Doesn't function, but would have altered a data value inside the Guest class object to mark them as having been seated
def seated():
    Reservation.update_seated_status()

# Defining Menu Functions
# All the functions below simply close the current menu and open the next menu

def close_menus():
    frameLogin.pack_forget()
    frameMain.pack_forget()
    frameHost.pack_forget()
    frameServer.pack_forget()
    frameAppetizer.pack_forget()
    frameEntree.pack_forget()
    frameDessert.pack_forget()
    frameDrink.pack_forget()
    frameAlcohol.pack_forget()

# This function does as said above, except it brings you back to the start of the application so that you can enter a different pin
def relogin():
    close_menus()
    frameLogin.pack(fill="both", expand=1)

# This does as said above, except if you input a pin that locked the "Server" button you would instead be sent to the host menu rather
# than the login screen because it would mean you used the "Carryout" button inside the host menu, otherwise it returns you to the login
# screen at the start of the application
def relogin_selective():
    close_menus()
    if button_m2["state"]==DISABLED:
        frameHost.pack(fill="both", expand=1)
    else:
        frameLogin.pack(fill="both", expand=1)

def main_menu():
    close_menus()
    frameMain.pack(fill="both", expand=1)

def host_menu():
    close_menus()
    frameHost.pack(fill="both", expand=1)

def reservation_menu():
    close_menus()
    frameReservation.pack(fill="both", expand=1)

def server_menu():
    close_menus()
    frameServer.pack(fill="both", expand=1)

def appetizer_menu():
    close_menus()
    frameAppetizer.pack(fill="both", expand=1)

def entree_menu():
    close_menus()
    frameEntree.pack(fill="both", expand=1)

def dessert_menu():
    close_menus()
    frameDessert.pack(fill="both", expand=1)

def drink_menu():
    close_menus()
    frameDrink.pack(fill="both", expand=1)

def alcohol_menu():
    close_menus()
    frameAlcohol.pack(fill="both", expand=1)

# Creating Labels for each menu
loginLabel = Label(frameLogin, text="Pin Login", bg="black", fg="red", font= 36)
mainLabel = Label(frameMain, text="Main Menu", bg="black", fg="red", font= 36)
hostLabel = Label(frameHost, text="Host", bg="black", fg="red", font= 36)
reservationLabel = Label(frameReservation, text="Reservations", bg="black", fg="red", font= 36)
reservationLabel2 = Label(frameReservation, text="(Non-Functional)", bg="black", fg="red", font= 36)
serverLabel = Label(frameServer, text="Dining Menu", bg="black", fg="red", font= 36)
appetizerLabel = Label(frameAppetizer, text="Appetizers", bg="black", fg="red", font= 36)
entreeLabel = Label(frameEntree, text="Entrées", bg="black", fg="red", font= 36)
dessertLabel = Label(frameDessert, text="Desserts", bg="black", fg="red", font= 36)
drinkLabel = Label(frameDrink, text="Drinks", bg="black", fg="red", font= 36)
alcoholLabel = Label(frameAlcohol, text="Alcohol", bg="black", fg="red", font= 36)

# Creating Buttons

# Login Menu
button_1=Button(frameLogin, text="1", padx=20, pady=15, bg="grey", fg="black", command=lambda:buttonNum(1))
button_2=Button(frameLogin, text="2", padx=20, pady=15, bg="grey", fg="black", command=lambda:buttonNum(2))
button_3=Button(frameLogin, text="3", padx=20, pady=15, bg="grey", fg="black", command=lambda:buttonNum(3))
button_4=Button(frameLogin, text="4", padx=20, pady=15, bg="grey", fg="black", command=lambda:buttonNum(4))
button_5=Button(frameLogin, text="5", padx=20, pady=15, bg="grey", fg="black", command=lambda:buttonNum(5))
button_6=Button(frameLogin, text="6", padx=20, pady=15, bg="grey", fg="black", command=lambda:buttonNum(6))
button_7=Button(frameLogin, text="7", padx=20, pady=15, bg="grey", fg="black", command=lambda:buttonNum(7))
button_8=Button(frameLogin, text="8", padx=20, pady=15, bg="grey", fg="black", command=lambda:buttonNum(8))
button_9=Button(frameLogin, text="9", padx=20, pady=15, bg="grey", fg="black", command=lambda:buttonNum(9))
button_0=Button(frameLogin, text="0", padx=20, pady=15, bg="grey", fg="black", command=lambda:buttonNum(0))
button_clear=Button(frameLogin, text="Clear", padx=10, pady=15, bg="grey", fg="black", command=clear)
button_enter=Button(frameLogin, text="Enter", padx=10, pady=15, bg="grey", fg="black", command=enter)

# Main Menu
button_m1=Button(frameMain, text="Host Menu", padx=20, pady=15, bg="grey", fg="black", command=host_menu)
button_m2=Button(frameMain, text="Server Menu", padx=20, pady=15, bg="grey", fg="black", command=server_menu)

# Host Menu
button_h1=Button(frameHost, text="Reservation List", padx=20, pady=15, bg="grey", fg="black", command=reservation_menu)
button_h2=Button(frameHost, text="Carryout", padx=20, pady=15, bg="grey", fg="black", command=server_menu)
button_hExit=Button(frameHost, text="X|Exit|X", padx=20, pady=15, bg="red", fg="white", command=relogin)

# Reservation Menu
button_r1=Button(frameReservation, text="<-", padx=20, pady=15, bg="grey", fg="black")
button_r2=Button(frameReservation, text="->", padx=20, pady=15, bg="grey", fg="black")
button_r3=Button(frameReservation, text="Add", padx=20, pady=15, bg="grey", fg="black", command=addReservation)
button_r4=Button(frameReservation, text="Seated", padx=20, pady=15, bg="grey", fg="black", command=seated)
button_rExit=Button(frameReservation, text="X|Exit|X", padx=20, pady=15, bg="red", fg="white", command=host_menu)

# Server Menu
button_s1=Button(frameServer, text="Appetizers", padx=20, pady=15, bg="grey", fg="black", command=appetizer_menu)
button_s2=Button(frameServer, text="Entrées", padx=20, pady=15, bg="grey", fg="black", command=entree_menu)
button_s3=Button(frameServer, text="Desserts", padx=20, pady=15, bg="grey", fg="black", command=dessert_menu)
button_s4=Button(frameServer, text="Drinks", padx=20, pady=15, bg="grey", fg="black", command=drink_menu)
button_s5=Button(frameServer, text="Alcohol", padx=20, pady=15, bg="grey", fg="black", command=alcohol_menu)
button_s6=Button(frameServer, text="|Order|", padx=20, pady=15, bg="blue", fg="white", command=placeOrder)
button_sExit=Button(frameServer, text="X|Exit|X", padx=20, pady=15, bg="red", fg="white", command=relogin_selective)

# Server Menu (Sub Menus)

# Appetizer
button_ap1=Button(frameAppetizer, text="Fried Pickles", padx=20, pady=15, bg="grey", fg="black", command=lambda:appButton(0))
button_ap2=Button(frameAppetizer, text="Cheese Sticks", padx=20, pady=15, bg="grey", fg="black", command=lambda:appButton(1))
button_ap3=Button(frameAppetizer, text="Tortilla Chips", padx=20, pady=15, bg="grey", fg="black", command=lambda:appButton(2))
button_ap4=Button(frameAppetizer, text="Onion rings", padx=20, pady=15, bg="grey", fg="black", command=lambda:appButton(3))
button_ap5=Button(frameAppetizer, text="Boneless Wings", padx=18, pady=15, bg="grey", fg="black", command=lambda:appButton(4))
button_apExit=Button(frameAppetizer, text="X|Exit|X", padx=20, pady=15, bg="red", fg="white", command=server_menu)

# Entree
button_e1=Button(frameEntree, text="Hand Crafted Burger", padx=20, pady=15, bg="grey", fg="black", command=lambda:entreeButton(0))
button_e2=Button(frameEntree, text="Grilled Atlantic Salmon", padx=20, pady=15, bg="grey", fg="black", command=lambda:entreeButton(1))
button_e3=Button(frameEntree, text="Ultimate Mac & Cheese", padx=20, pady=15, bg="grey", fg="black", command=lambda:entreeButton(2))
button_e4=Button(frameEntree, text="Fish and Chips", padx=20, pady=15, bg="grey", fg="black", command=lambda:entreeButton(3))
button_e5=Button(frameEntree, text="1/2 Ribs", padx=20, pady=15, bg="grey", fg="black", command=lambda:entreeButton(4))
button_eExit=Button(frameEntree, text="X|Exit|X", padx=20, pady=15, bg="red", fg="white", command=server_menu)

# Dessert
button_de1=Button(frameDessert, text="Fudge Brownie", padx=20, pady=15, bg="grey", fg="black", command=lambda:desButton(0))
button_de2=Button(frameDessert, text="Peanut Butter Brownie", padx=5, pady=15, bg="grey", fg="black", command=lambda:desButton(1))
button_de3=Button(frameDessert, text="Cheesecake", padx=20, pady=15, bg="grey", fg="black", command=lambda:desButton(2))
button_de4=Button(frameDessert, text="Vanilla Cake", padx=20, pady=15, bg="grey", fg="black", command=lambda:desButton(3))
button_de5=Button(frameDessert, text="Bread Pudding", padx=20, pady=15, bg="grey", fg="black", command=lambda:desButton(4))
button_deExit=Button(frameDessert, text="X|Exit|X", padx=20, pady=15, bg="red", fg="white", command=server_menu)

# Drink
button_dr1=Button(frameDrink, text="Coca Cola", padx=20, pady=15, bg="grey", fg="black", command=lambda:drinkButton(0))
button_dr2=Button(frameDrink, text="Sprite", padx=20, pady=15, bg="grey", fg="black", command=lambda:drinkButton(1))
button_dr3=Button(frameDrink, text="Sweet Tea", padx=20, pady=15, bg="grey", fg="black", command=lambda:drinkButton(2))
button_dr4=Button(frameDrink, text="Unsweet Tea", padx=20, pady=15, bg="grey", fg="black", command=lambda:drinkButton(3))
button_dr5=Button(frameDrink, text="Water", padx=20, pady=15, bg="grey", fg="black", command=lambda:drinkButton(4))
button_drExit=Button(frameDrink, text="X|Exit|X", padx=20, pady=15, bg="red", fg="white", command=server_menu)

# Alcohol
button_al1=Button(frameAlcohol, text="Long Island Iced Tea", padx=5, pady=15, bg="grey", fg="black", command=lambda:alcButton(0))
button_al2=Button(frameAlcohol, text="Old Fashioned", padx=20, pady=15, bg="grey", fg="black", command=lambda:alcButton(1))
button_al3=Button(frameAlcohol, text="Margarita", padx=20, pady=15, bg="grey", fg="black", command=lambda:alcButton(2))
button_al4=Button(frameAlcohol, text="Hurricane", padx=20, pady=15, bg="grey", fg="black", command=lambda:alcButton(3))
button_al5=Button(frameAlcohol, text="Mint Julep", padx=20, pady=15, bg="grey", fg="black", command=lambda:alcButton(4))
button_alExit=Button(frameAlcohol, text="X|Exit|X", padx=20, pady=15, bg="red", fg="white", command=server_menu)

# Put Widgets on Screen

# Login
loginLabel.grid(row=0, columnspan=3)
entry.grid(row=1, columnspan=3, sticky=N+E+S+W)
button_1.grid(row=2, column=0, sticky=N+E+S+W)
button_2.grid(row=2, column=1, sticky=N+E+S+W)
button_3.grid(row=2, column=2, sticky=N+E+S+W)
button_4.grid(row=3, column=0, sticky=N+E+S+W)
button_5.grid(row=3, column=1, sticky=N+E+S+W)
button_6.grid(row=3, column=2, sticky=N+E+S+W)
button_7.grid(row=4, column=0, sticky=N+E+S+W)
button_8.grid(row=4, column=1, sticky=N+E+S+W)
button_9.grid(row=4, column=2, sticky=N+E+S+W)
button_0.grid(row=5, column=1, sticky=N+E+S+W)
button_clear.grid(row=5, column=0, sticky=N+E+S+W)
button_enter.grid(row=5, column=2, sticky=N+E+S+W)

# Main
mainLabel.grid(row=0, column=0)
button_m1.grid(row=1, column=0, sticky=N+E+S+W)
button_m2.grid(row=2, column=0, sticky=N+E+S+W)

# Host
hostLabel.grid(row=0, column=0)
button_h1.grid(row=2, column=0, sticky=N+E+S+W)
button_h2.grid(row=1, column=0, sticky=N+E+S+W)
button_hExit.grid(row=3, column=0, sticky=N+E+S+W)

# Reservation
reservationLabel.grid(row=0, columnspan=4)
reservationLabel2.grid(row=1, columnspan=4)
button_r1.grid(row=2, column=0, sticky=N+E+S+W)
button_r2.grid(row=2, column=3, sticky=N+E+S+W)
button_r3.grid(row=2, column=1, sticky=N+E+S+W)
button_r4.grid(row=2, column=2, sticky=N+E+S+W)
button_rExit.grid(row=3, columnspan=4, sticky=N+E+S+W)

# Server
serverLabel.grid(row=0, columnspan=2)
button_s1.grid(row=1, columnspan=2, sticky=N+E+S+W)
button_s2.grid(row=2, column=0, sticky=N+E+S+W)
button_s3.grid(row=2, column=1, sticky=N+E+S+W)
button_s4.grid(row=3, column=0, sticky=N+E+S+W)
button_s5.grid(row=3, column=1, sticky=N+E+S+W)
button_s6.grid(row=4, columnspan=2, sticky=N+E+S+W)
button_sExit.grid(row=5, columnspan=2, sticky=N+E+S+W)

# Appetizer
appetizerLabel.grid(row=0, columnspan=2)
button_ap1.grid(row=1, column=0, sticky=N+E+S+W)
button_ap2.grid(row=1, column=1, sticky=N+E+S+W)
button_ap3.grid(row=2, column=0, sticky=N+E+S+W)
button_ap4.grid(row=2, column=1, sticky=N+E+S+W)
button_ap5.grid(row=3, column=0, sticky=N+E+S+W)
button_apExit.grid(row=3, column=1, sticky=N+E+S+W)

# Entree
entreeLabel.grid(row=0, columnspan=2)
button_e1.grid(row=1, column=0, sticky=N+E+S+W)
button_e2.grid(row=1, column=1, sticky=N+E+S+W)
button_e3.grid(row=2, column=0, sticky=N+E+S+W)
button_e4.grid(row=2, column=1, sticky=N+E+S+W)
button_e5.grid(row=3, column=0, sticky=N+E+S+W)
button_eExit.grid(row=3, column=1, sticky=N+E+S+W)

# Dessert
dessertLabel.grid(row=0, columnspan=2)
button_de1.grid(row=1, column=0, sticky=N+E+S+W)
button_de2.grid(row=1, column=1, sticky=N+E+S+W)
button_de3.grid(row=2, column=0, sticky=N+E+S+W)
button_de4.grid(row=2, column=1, sticky=N+E+S+W)
button_de5.grid(row=3, column=0, sticky=N+E+S+W)
button_deExit.grid(row=3, column=1, sticky=N+E+S+W)

# Drink
drinkLabel.grid(row=0, columnspan=2)
button_dr1.grid(row=1, column=0, sticky=N+E+S+W)
button_dr2.grid(row=1, column=1, sticky=N+E+S+W)
button_dr3.grid(row=2, column=0, sticky=N+E+S+W)
button_dr4.grid(row=2, column=1, sticky=N+E+S+W)
button_dr5.grid(row=3, column=0, sticky=N+E+S+W)
button_drExit.grid(row=3, column=1, sticky=N+E+S+W)

# Alcohol
alcoholLabel.grid(row=0, columnspan=2)
button_al1.grid(row=1, column=0, sticky=N+E+S+W)
button_al2.grid(row=1, column=1, sticky=N+E+S+W)
button_al3.grid(row=2, column=0, sticky=N+E+S+W)
button_al4.grid(row=2, column=1, sticky=N+E+S+W)
button_al5.grid(row=3, column=0, sticky=N+E+S+W)
button_alExit.grid(row=3, column=1, sticky=N+E+S+W)










# The below line is required for tkinter to open the initial window
TK.mainloop()