def isLeapYear(a):
    returnvalue = 0
    if (a % 4 == 0):
        if (a % 100 == 0):
            returnvalue = 1
            if (a % 400 == 0):
                returnvalue = 2
    else :
        returnvalue = 1
    return (returnvalue)

def main():
    print ("This program determines if a year is a leap year.")
    year = int(input("Enter a year: "))
    if ((isLeapYear(year) % 2 == 0)):
        print (year, "is a leap year.")
    else :
        print (year, "is not a leap year.")

main()
