from FoodMenu import *
from Menu import *
from Billing import *
from Reservations import *

billAmt = [] #Creates list of bills returned from the menuSelection function
billItems = [] #Creates a list of lists returned from the menuSelection function
originalBillAmt = [] #I created this list just to help with the billing function
customerNumber = 1
maxCustomers = 1 #Helps keep track of number of customers and keeping them in sequential order
customerSelection = 0
exit = False

while(exit == False):
    userInput = int(input("Which menu would you like to use? \n1. Food Menu\n2. Billing\n3. Reservation\n4. Exit Menu\n"))
    
    if(userInput == 1):
        customerNumber = int(input("Please enter the customer number: "))
        if(customerNumber > (maxCustomers + 1)):
            print("Invalid customer number entered. Returning to menu.\n")
        elif(customerNumber == (maxCustomers + 1)):
            maxCustomers = customerNumber
            print("\n")
            bill, billList = menuSelection()
            billAmt.append(bill)
            originalBillAmt.append(bill)
            billItems.append(billList)
        elif(customerNumber <= maxCustomers):
            print("\n")
            bill, billList = menuSelection()
            billAmt.append(bill)
            billItems.append(billList)
            originalBillAmt.append(bill)


    if(userInput == 2):
        customerNumber = int(input("Please enter the customer number: "))
        if(customerNumber > maxCustomers):
            print("Invalid customer number entered. Returning to menu.\n")
        elif(customerNumber <= maxCustomers):
            print("\n")
            billAmt[customerNumber - 1] = handleBill(billAmt[customerNumber - 1], billItems[customerNumber - 1], originalBillAmt[customerNumber - 1])
            print("Bill Amount is: ",billAmt[customerNumber - 1])
            
    if(userInput == 3):
        userInput = int(input("1. Add Reservation \n2. Seat Reservation\n"))
        if(userInput == 1):
            add_guest_reservation()#should be activated by button click in the UI
        if(userInput == 2):
            seat_guest()#should be activated by button click in the UI
        
    if(userInput == 4):
        finalAnswer = input("Are you sure you want to close? 'y' for yes, 'n' for no: ")
        if(finalAnswer == "y"):
            exit = True
        elif(finalAnswer == "n"):
            print("Returning to Menu")
        elif(finalAnswer != "y" or finalAnswer != "n"):
            print("Invalid selection. Returning to menu.\n")
