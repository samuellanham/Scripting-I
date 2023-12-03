print ("This program adds odd numbers, and multiplies even numbers.")
print ("Enter 0 or a negative number to exit.")

number = int(input("Enter a positive integer: "))
summation = 0

while (number > 0):
    if ((number % 2) == 0):
        summation *= number
    else :
        summation += number
    number = int(input("Enter a positive integer: "))

print ("The final number is", summation)
