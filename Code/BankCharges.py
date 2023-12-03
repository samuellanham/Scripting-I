checks = int(input("How many checks written for the month: "))

if (checks < 0):
    print ("Please enter a positive number.")
else :
    print ("Number of Checks:", checks)
    if (checks < 20):
        fees = checks * 0.10 + 10
    elif (checks < 40):
        fees = checks * 0.08 + 10
    elif (checks < 60):
        fees = checks * 0.06 + 10
    else :
        fees = checks * 0.04 + 10
    print ("Total Fees: $" + "{:,.2f}".format(fees))
