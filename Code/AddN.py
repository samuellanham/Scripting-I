numbers = int(input("How many numbers should I add? "))

total = 0

for x in range (numbers):
    integer = float(input("Enter a number: "))
    total += integer

print ()
print ("The total is " + "{:,.1f}".format(total))
