def handleBill(bill, billItems, originalBill):
    i = 0
    taxRate = .07
    paid = 0.00
    change = 0.00
    tax = (taxRate * bill)
    #The below if/elif statement is there so it can properly calculate bill
    #based on whether or not they had partially paid already.
    if(originalBill == bill):
        totalBill = bill + tax
    elif(bill != originalBill):
        totalBill = bill
    while(i < len(billItems)):
        print(billItems[i].getName(), " ", billItems[i].getPrice())
        i += 1
    print("")
    print("Bill is:", "%.2f" %bill)
    #The below if statement displays tax as zero if there was a partial payment already.
    #Taxes were already added into the bill the first time they partially paid.
    if(originalBill != bill):
        tax = 0.00
    print("Tax:", "%.2f" %tax)
    print("Total Bill:", "%.2f" %totalBill, "\n")
    print("Items: ")

    while True:
        paid = float(input("Please enter amount paid: "))
        if(paid <= 0):
            print("Invalid Amount Entered.")
        elif(paid > 0):
            break
    change = (totalBill - paid)
    if(change > 0): #Returns change as new bill
        print("Customer still has a balance of: ", "%.2f" %change,"\n")
        return change
    elif(change < 0): #Displays amount due back to customer and returns 0 for bill
        change = (change * -1)
        print("Bill is paid in full. Please return change of: ", "%.2f" %change,"\n")
        return 0
    elif(change == 0): #Returns 0 for bill
        print("Bill is paid in full.\n")
        return 0