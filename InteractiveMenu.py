from Menu import Menu, Appetizer, Entree, Dessert, Drink, Alcohol

billList = [] #Creates final bill list for output
appToAddList = [] #Any appetizers added to order are put in this list
entreeToAddList = [] #Any entrees added to order are put in this list
dessertToAddList = [] #Any desserts added to order are put in this list
drinkToAddList = [] #Any drinks added to order are put in this list
alcoholToAddList = [] #Any alcoholic beverages added to order are in this list
appList = [] #List of appetizers
appList.append(Appetizer("Fried Pickles", 6.35, False))
appList.append(Appetizer("Cheese Sticks", 8.95, False))
appList.append(Appetizer("Tortilla Chips", 3.65, False))
appList.append(Appetizer("Onion Rings", 6.95, False))
appList.append(Appetizer("Boneless Wings", 11.95, False))

entreeList = [] #List of Entrees
entreeList.append(Entree("Hand Crafted Burger", 14.95, False, False))
entreeList.append(Entree("Grilled Atlantic Salmon", 21.95, False, False))
entreeList.append(Entree("Ultimate Mac and Cheese", 16.95, False, False))
entreeList.append(Entree("Fish and Chips", 15.80, False, False))
entreeList.append(Entree("1/2 Ribs", 23.15, False, False))

dessertList = [] #List of desserts
dessertList.append(Dessert("Fudge Brownie", 8.45, False))
dessertList.append(Dessert("Peanut Butter Brownie", 9.65, False))
dessertList.append(Dessert("Cheesecake", 4.50, False))
dessertList.append(Dessert("Vanilla Cake", 5.00, False))
dessertList.append(Dessert("Bread Pudding", 7.15, False))

drinkList = [] #List of drinks
drinkList.append(Drink("Coke", 2.95, False, False))
drinkList.append(Drink("Sprite", 2.95, False, False))
drinkList.append(Drink("Sweet Tea", 2.95, False, False))
drinkList.append(Drink("Unsweet Tea", 2.95, False, False))
drinkList.append(Drink("Water", 0.00, False, False))

alcoholList = [] #List of alcohol
alcoholList.append(Alcohol("Long Island Iced Tea", 12.95, False, False))
alcoholList.append(Alcohol("Old Fashioned", 11.55, False, False))
alcoholList.append(Alcohol("Margarita", 14.15, False, False))
alcoholList.append(Alcohol("Hurricane", 12.85, False, False))
alcoholList.append(Alcohol("Mint Julep", 9.95, False, False))

bill = 0.00
userInput = 0

#   MESSAGE FROM JOSH TO LOGAN
#   I did not add any input validation because these menus are supposed to be
#   accessed through clicking menu buttons through the POS. That being said, that
#   is why I have weird breakout conditions to traverse the menus such as using
#   100 to break out of the while loops. The idea is that to go back to a previous
#   menu a user should just be able to click a "Back" button. That button should
#   trigger the input to be read as "100". Same thing with "6" being the exit condition
#   to leave the menu altogether. There should be a back button that when clicked 
#   acts like "6" was entered to breakout.



#   So this program is mostly made up of if statements. I will leave documentation
#   in the first if statement so that it makes sense, and then every other elif
#   statement after will be structured similarly.







while(userInput != 6):
    appChoice = 0 #Lines 70 - 74 are just initialization every time the loop goes through
    entreeChoice = 0
    dessertChoice = 0
    drinkChoice = 0
    alcoholChoice = 0
    userInput = int(input("Choose the menu you would like to see: "))
    if(userInput == 1):
        while(appChoice != 100): #Breakout condition I mentioned above
            count = 0
            print("\nAppetizer List:")
            while(count < len(appList)): #Just prints everything in appList
                print(appList[count].getName())
                count += 1
            appChoice = int(input("\nChoose which appetizers to add: "))
            if(appChoice == 100):
                print("\n")
                break
            bill += appList[appChoice - 1].getPrice() #Adds to bill variable
            addBread = int(input("Add bread to appetizer? "))
            if(addBread == 1):
                setAddBread = True;
                bill += 1.00
            else:
                setAddBread = False;
            #I create a new Appetizer object and put it into appToAddList
            appToAddList.append(Appetizer(appList[appChoice - 1].getName(), appList[appChoice - 1].getPrice(), setAddBread))
        
    elif(userInput == 2):
        while(entreeChoice != 100):
            count = 0
            print("\nEntree List:")
            while(count < len(entreeList)):
                print(entreeList[count].getName())
                count += 1
            entreeChoice = int(input("\nChoose which entrees to add: "))
            if(entreeChoice == 100):
                print("\n")
                break
            bill += entreeList[entreeChoice - 1].getPrice()
            addSoup = int(input("Add soup to entree? "))
            addSalad = int(input("Add salad to entree? "))
            if(addSoup == 1):
                setAddSoup = True
                bill += 2.00
            else:
                setAddSoup = False
            if(addSalad == 1):
                setAddSalad = True
                bill += 2.00
            else:
                setAddSalad = False
            entreeToAddList.append(Entree(entreeList[entreeChoice - 1].getName(), entreeList[entreeChoice - 1].getPrice(), setAddSoup, setAddSalad))
        
    elif(userInput == 3):
        while(dessertChoice != 100):
            count = 0
            print("\nDessert List:")
            while(count < len(dessertList)):
                print(dessertList[count].getName())
                count += 1
            dessertChoice = int(input("\nChoose which desserts to add: "))
            if(dessertChoice == 100):
                print("\n")
                break
            bill += dessertList[dessertChoice - 1].getPrice()
            addAlaMode = int(input("Make dessert a la mode? "))
            if(addAlaMode == 1):
                setAddAlaMode = True
                bill += 2.00
            else:
                setAddAlaMode = False
            dessertToAddList.append(Dessert(dessertList[dessertChoice - 1].getName(), dessertList[dessertChoice - 1].getPrice(), setAddAlaMode))
            
    elif(userInput == 4):
        while(drinkChoice != 100):
            count = 0
            print("\nDrink List:")
            while(count < len(drinkList)):
                print(drinkList[count].getName())
                count += 1
            drinkChoice = int(input("\nChoose which drinks to add: "))
            if(drinkChoice == 100):
                print("\n")
                break
            bill += drinkList[drinkChoice - 1].getPrice()
            addLemon = int(input("Add lemon? "))
            if(addLemon == 1):
                setAddLemon = True
            else:
                setAddLemon = False
            addSugar = int(input("Add sugar? "))
            if(addSugar == 1):
                setAddSugar = True
            else:
                setAddSugar = False
            drinkToAddList.append(Drink(drinkList[drinkChoice - 1].getName(), drinkList[drinkChoice - 1].getPrice(), setAddLemon, setAddSugar))
            
    elif(userInput == 5):
        while(alcoholChoice != 100):
            count = 0
            print("\nAlcohol List:")
            while(count < len(alcoholList)):
                print(alcoholList[count].getName())
                count += 1
            alcoholChoice = int(input("\nChoose which alcoholic beverages to add: "))
            if(alcoholChoice == 100):
                print("\n")
                break
            bill += alcoholList[alcoholChoice - 1].getPrice()
            addWhippedCream = int(input("Add whipped cream? "))
            if(addWhippedCream == 1):
                setAddWhippedCream = True
            else:
                setAddWhippedCream = False
            addDoubleShot = int(input("Add double shot? "))
            if(addDoubleShot == 1):
                setAddDoubleshot = True
                bill += 3.00
            else:
                setAddDoubleshot = False
            alcoholToAddList.append(Alcohol(alcoholList[alcoholChoice - 1].getName(), alcoholList[alcoholChoice - 1].getPrice(), setAddWhippedCream, setAddDoubleshot))
            
            
            
#   So the lines from 195 - 220 actually check all of the lists we made above.
#   If something is in those lists, we put them in order categorically into 
#   billList. This just makes output look nicer and like an actual bill would.
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

#   This final bit here just displays everything added to bill. The output is not
#   spaced quite how I would like it, but I may reiterate on that part later. If 
#   either one of you would like to format it so that it looks nice, please feel 
#   as free as an American. It also needs adjusted so that it always displays 
#   two decimal points.
count = 0
while(count < len(billList)):
    print(billList[count].getName(), " ", billList[count].getPrice())
    count += 1
print("\n")
print("Final Bill Amount: $", bill)