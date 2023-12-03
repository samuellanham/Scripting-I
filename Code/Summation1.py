print ("This program calculates the sum of all integers from 1 to the input value.")
integer = int(input("Please enter an integer: "))

count = 1
summation = 0

while (count <= integer):
    summation = summation + count
    count = count + 1

print (summation)
