number = int(input("Which number would you like to see the multiplication table for? "))
lowest = int(input("What is the lowest number for the table? "))
highest = int(input("What is the highest number for the table? "))

for x in range (lowest, highest):
    print (number, "*", x, "=", number * x)
