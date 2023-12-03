print ("Enter a list of numbers, using a negative number to indicate that you are done.")

number = 0.0
summation = 0.0

while (number >= 0.0):
    summation += number
    number = float(input("Enter a number: "))

print()
print ("The total is", summation)
