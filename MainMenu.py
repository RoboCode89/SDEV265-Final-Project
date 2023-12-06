from FoodMenu import *
from Menu import *

count = 1
maxCount = 1
customerSelection = 0
exit = False

while(exit == False):
    userInput = int(input("Which menu would you like to use? \n1. Food Menu\n2. Billing\n3. Reservation\n4. Exit Menu\n"))
    
    if(userInput == 1):
        count = int(input("Please enter the customer number: "))
        if(count > (maxCount + 1)):
            print("Invalid customer number entered. Returning to menu.\n")
        elif(count == (maxCount + 1) or count <= maxCount):
            maxCount = count
            print("\n")
            bill, billList = menuSelection()
            
    '''if(userInput == 2):
        count = int(input("Please enter the customer number: "))
        if(count > maxCount):
            print("Invalid customer number entered. Returning to menu.\n")
        elif(count <= maxCount):
            billing(bill[count], billList[count])
            
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


i = 0
print("Bill is", "%.2f" %bill)
print("Items Chosen: ")
while(i < len(billList)):
    print(billList[i].getName(), " ", billList[i].getPrice())
    i += 1
    
    
    
