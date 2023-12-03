print ("This program calculates the price to enter a zoo based on age.")
age = int(input("Enter your age: "))
print ("You entered age", age)

if (age < 3):
    print ("Admission is free.")
else :
    if (age < 11):
        admission = 5
    elif (age < 21):
        admission = 10
    elif (age < 60):
        admission = 20
    else :
        admission = 10
    print ("Admission is $" + "{:,.0f}".format(admission) + ".")
