print ("This program calculates the sum of all integers from the first input value to the second input value.")

integer1 = int(input("Please enter an integer: "))
integer2 = int(input("Please enter an integer: "))

count = integer1
summation = integer1

while (count < integer2):
    count = count + 1
    summation = summation + count

print (summation)
