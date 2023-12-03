print ("This program determines whether you may get a loan.")

income = int(input("Please enter your income in dollars: "))
credit = int(input("Please enter your credit rating: "))
collateral = str(input("Please enter if you are using collateral (yes or no): "))

if ((income >= 50000 and credit >= 600) or (collateral == "yes")):
    print ("Approved!")
else :
    print ("We are sorry, but you are not approved.")
