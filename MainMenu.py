
    
from FoodMenu import *
from Menu import *

billAmt = []
billItems = []
customerNumber = 1
maxCustomers = 1
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
        elif(customerNumber <= maxCustomers):
            print("\n")
            bill, billList = menuSelection()
            billAmt.append(bill)
            billItems.append(billList)


    '''if(userInput == 2):
        customerNumber = int(input("Please enter the customer number: "))
        if(customerNumber > maxCustomers):
            print("Invalid customer number entered. Returning to menu.\n")
        elif(count <= maxCount):
            billing(billAmt[customerNumber - 1], billItems[customerNumber - 1])
            
    if(userInput == 3):
        reservation() '''
        
    if(userInput == 4):
        finalAnswer = input("Are you sure you want to close? 'y' for yes, 'n' for no: ")
        if(finalAnswer == "y"):
            exit = True
        elif(finalAnswer == "n"):
            print("Returning to Menu")
        elif(finalAnswer != "y" or finalAnswer != "n"):
            print("Invalid selection. Returning to menu.\n")


'''i = 0
print("Bill is", "%.2f" %bill)
print("Items Chosen: ")
        while(i < len(billItems[0])): #Doing it this way allows to select specific billItems for customer using double array
            print(billItems[0][i].getName(), " ", billItems[0][i].getPrice())
            i += 1'''
