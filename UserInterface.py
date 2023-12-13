from tkinter import *
from newlogin import *

TK = Tk()

# Providing Settings for Initial Window
TK.title("Restaurant POS")

wHeight = 400
wWidth = 700

sHeight = TK.winfo_screenheight()
sWidth = TK.winfo_screenwidth()

x = (sWidth / 2) - (wWidth / 2)
y = (sHeight / 2) - (wHeight / 2)

TK.geometry(f'{wWidth}x{wHeight}+{int(x)}+{int(y)}')

# Creating Frames

frameLogin = Frame(TK, width=wWidth, height=wHeight, padx=wWidth/2.9, pady=wHeight/5, bg="black")
frameMain = Frame(TK, width=wWidth, height=wHeight, padx=wWidth/2.45, pady=wHeight/5, bg="black")
frameHost = Frame(TK, width=wWidth, height=wHeight, padx=wWidth/2.5, pady=wHeight/5, bg="black")
frameServer = Frame(TK, width=wWidth, height=wHeight, padx=wWidth/2.7, pady=wHeight/5, bg="black")
frameAppetizer = Frame(TK, width=wWidth, height=wHeight, padx=wWidth/3.2, pady=wHeight/5, bg="black")
frameEntree = Frame(TK, width=wWidth, height=wHeight, padx=wWidth/4, pady=wHeight/5, bg="black")
frameDessert = Frame(TK, width=wWidth, height=wHeight, padx=wWidth/3.2, pady=wHeight/5, bg="black")
frameDrink = Frame(TK, width=wWidth, height=wHeight, padx=wWidth/2.9, pady=wHeight/5, bg="black")
frameAlcohol = Frame(TK, width=wWidth, height=wHeight, padx=wWidth/3.2, pady=wHeight/5, bg="black")
frameLogin.pack(fill="both", expand=1)

# Creating an entry box
e = Entry(frameLogin, width=30, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=5, sticky=N+E+S+W)

# Defining Reused Functions

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

def buttonNum(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current)+str(number))

def enter():
    current = e.get()
    if int(current)<1000 or int(current)>9999:
        clear()
        e.insert(0, "Enter a 4 digit pin (Clear First)")
    else:
        Login.employee_login()

def clear():
    e.delete(0, END)

# Defining Single-Use Functions

def relogin():
    close_menus()
    frameLogin.pack(fill="both", expand=1)

def relogin_selective():
    close_menus()
    frameLogin.pack(fill="both", expand=1)

def main_menu():
    close_menus()
    frameMain.pack(fill="both", expand=1)

def host_menu():
    close_menus()
    frameHost.pack(fill="both", expand=1)

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
button_h1=Button(frameHost, text="Reservation List", padx=20, pady=15, bg="grey", fg="black")
button_h2=Button(frameHost, text="Carryout", padx=20, pady=15, bg="grey", fg="black")
button_hExit=Button(frameHost, text="X|Exit|X", padx=20, pady=15, bg="red", fg="white", command=relogin)

# Server Menu
button_s1=Button(frameServer, text="Appetizers", padx=20, pady=15, bg="grey", fg="black", command=appetizer_menu)
button_s2=Button(frameServer, text="Entrées", padx=20, pady=15, bg="grey", fg="black", command=entree_menu)
button_s3=Button(frameServer, text="Desserts", padx=20, pady=15, bg="grey", fg="black", command=dessert_menu)
button_s4=Button(frameServer, text="Drinks", padx=20, pady=15, bg="grey", fg="black", command=drink_menu)
button_s5=Button(frameServer, text="Alcohol", padx=20, pady=15, bg="grey", fg="black", command=alcohol_menu)
button_s6=Button(frameServer, text="|Order|", padx=20, pady=15, bg="blue", fg="white")
button_sExit=Button(frameServer, text="X|Exit|X", padx=20, pady=15, bg="red", fg="white", command=relogin_selective)

# Server Menu (Sub Menus)

# Appetizer
button_ap1=Button(frameAppetizer, text="Fried Pickles", padx=20, pady=15, bg="grey", fg="black")
button_ap2=Button(frameAppetizer, text="Cheese Sticks", padx=20, pady=15, bg="grey", fg="black")
button_ap3=Button(frameAppetizer, text="Tortilla Chips", padx=20, pady=15, bg="grey", fg="black")
button_ap4=Button(frameAppetizer, text="Onion rings", padx=20, pady=15, bg="grey", fg="black")
button_ap5=Button(frameAppetizer, text="Boneless Wings", padx=18, pady=15, bg="grey", fg="black")
button_apExit=Button(frameAppetizer, text="X|Exit|X", padx=20, pady=15, bg="red", fg="white", command=server_menu)

# Entree
button_e1=Button(frameEntree, text="Hand Crafted Burger", padx=20, pady=15, bg="grey", fg="black")
button_e2=Button(frameEntree, text="Grilled Atlantic Salmon", padx=20, pady=15, bg="grey", fg="black")
button_e3=Button(frameEntree, text="Ultimate Mac & Cheese", padx=20, pady=15, bg="grey", fg="black")
button_e4=Button(frameEntree, text="Fish and Chips", padx=20, pady=15, bg="grey", fg="black")
button_e5=Button(frameEntree, text="1/2 Ribs", padx=20, pady=15, bg="grey", fg="black")
button_eExit=Button(frameEntree, text="X|Exit|X", padx=20, pady=15, bg="red", fg="white", command=server_menu)

# Dessert
button_de1=Button(frameDessert, text="Fudge Brownie", padx=20, pady=15, bg="grey", fg="black")
button_de2=Button(frameDessert, text="Peanut Butter Brownie", padx=5, pady=15, bg="grey", fg="black")
button_de3=Button(frameDessert, text="Cheesecake", padx=20, pady=15, bg="grey", fg="black")
button_de4=Button(frameDessert, text="Vanilla Cake", padx=20, pady=15, bg="grey", fg="black")
button_de5=Button(frameDessert, text="Bread Pudding", padx=20, pady=15, bg="grey", fg="black")
button_deExit=Button(frameDessert, text="X|Exit|X", padx=20, pady=15, bg="red", fg="white", command=server_menu)

# Drink
button_dr1=Button(frameDrink, text="Coca Cola", padx=20, pady=15, bg="grey", fg="black")
button_dr2=Button(frameDrink, text="Sprite", padx=20, pady=15, bg="grey", fg="black")
button_dr3=Button(frameDrink, text="Sweet Tea", padx=20, pady=15, bg="grey", fg="black")
button_dr4=Button(frameDrink, text="Unsweet Tea", padx=20, pady=15, bg="grey", fg="black")
button_dr5=Button(frameDrink, text="Water", padx=20, pady=15, bg="grey", fg="black")
button_drExit=Button(frameDrink, text="X|Exit|X", padx=20, pady=15, bg="red", fg="white", command=server_menu)

# Alcohol
button_al1=Button(frameAlcohol, text="Long Island Iced Tea", padx=5, pady=15, bg="grey", fg="black")
button_al2=Button(frameAlcohol, text="Old Fashioned", padx=20, pady=15, bg="grey", fg="black")
button_al3=Button(frameAlcohol, text="Margarita", padx=20, pady=15, bg="grey", fg="black")
button_al4=Button(frameAlcohol, text="Hurricane", padx=20, pady=15, bg="grey", fg="black")
button_al5=Button(frameAlcohol, text="Mint Julep", padx=20, pady=15, bg="grey", fg="black")
button_alExit=Button(frameAlcohol, text="X|Exit|X", padx=20, pady=15, bg="red", fg="white", command=server_menu)

# Put Buttons on Screen

# Login
button_1.grid(row=1, column=0, sticky=N+E+S+W)
button_2.grid(row=1, column=1, sticky=N+E+S+W)
button_3.grid(row=1, column=2, sticky=N+E+S+W)
button_4.grid(row=2, column=0, sticky=N+E+S+W)
button_5.grid(row=2, column=1, sticky=N+E+S+W)
button_6.grid(row=2, column=2, sticky=N+E+S+W)
button_7.grid(row=3, column=0, sticky=N+E+S+W)
button_8.grid(row=3, column=1, sticky=N+E+S+W)
button_9.grid(row=3, column=2, sticky=N+E+S+W)
button_0.grid(row=4, column=1, sticky=N+E+S+W)
button_clear.grid(row=4, column=0, sticky=N+E+S+W)
button_enter.grid(row=4, column=2, sticky=N+E+S+W)

# Main
button_m1.grid(row=0, column=0, sticky=N+E+S+W)
button_m2.grid(row=1, column=0, sticky=N+E+S+W)

# Host
button_h1.grid(row=1, column=0, sticky=N+E+S+W)
button_h2.grid(row=0, column=0, sticky=N+E+S+W)
button_hExit.grid(row=2, column=0, sticky=N+E+S+W)

# Server
button_s1.grid(row=0, columnspan=2, sticky=N+E+S+W)
button_s2.grid(row=1, column=0, sticky=N+E+S+W)
button_s3.grid(row=1, column=1, sticky=N+E+S+W)
button_s4.grid(row=2, column=0, sticky=N+E+S+W)
button_s5.grid(row=2, column=1, sticky=N+E+S+W)
button_s6.grid(row=3, columnspan=2, sticky=N+E+S+W)
button_sExit.grid(row=4, columnspan=2, sticky=N+E+S+W)

# Appetizer
button_ap1.grid(row=0, column=0, sticky=N+E+S+W)
button_ap2.grid(row=0, column=1, sticky=N+E+S+W)
button_ap3.grid(row=1, column=0, sticky=N+E+S+W)
button_ap4.grid(row=1, column=1, sticky=N+E+S+W)
button_ap5.grid(row=2, column=0, sticky=N+E+S+W)
button_apExit.grid(row=2, column=1, sticky=N+E+S+W)

# Entree
button_e1.grid(row=0, column=0, sticky=N+E+S+W)
button_e2.grid(row=0, column=1, sticky=N+E+S+W)
button_e3.grid(row=1, column=0, sticky=N+E+S+W)
button_e4.grid(row=1, column=1, sticky=N+E+S+W)
button_e5.grid(row=2, column=0, sticky=N+E+S+W)
button_eExit.grid(row=2, column=1, sticky=N+E+S+W)

# Dessert
button_de1.grid(row=0, column=0, sticky=N+E+S+W)
button_de2.grid(row=0, column=1, sticky=N+E+S+W)
button_de3.grid(row=1, column=0, sticky=N+E+S+W)
button_de4.grid(row=1, column=1, sticky=N+E+S+W)
button_de5.grid(row=2, column=0, sticky=N+E+S+W)
button_deExit.grid(row=2, column=1, sticky=N+E+S+W)

# Drink
button_dr1.grid(row=0, column=0, sticky=N+E+S+W)
button_dr2.grid(row=0, column=1, sticky=N+E+S+W)
button_dr3.grid(row=1, column=0, sticky=N+E+S+W)
button_dr4.grid(row=1, column=1, sticky=N+E+S+W)
button_dr5.grid(row=2, column=0, sticky=N+E+S+W)
button_drExit.grid(row=2, column=1, sticky=N+E+S+W)

# Alcohol
button_al1.grid(row=0, column=0, sticky=N+E+S+W)
button_al2.grid(row=0, column=1, sticky=N+E+S+W)
button_al3.grid(row=1, column=0, sticky=N+E+S+W)
button_al4.grid(row=1, column=1, sticky=N+E+S+W)
button_al5.grid(row=2, column=0, sticky=N+E+S+W)
button_alExit.grid(row=2, column=1, sticky=N+E+S+W)










# The below line is required for tkinter to open the initial window
TK.mainloop()