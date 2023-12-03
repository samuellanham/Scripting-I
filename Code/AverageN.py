print ("This program averages numbers.")
print ()

total = 0.0
count = 0

numbers = int(input("How many numbers? "))
for x in range (numbers):
    integer = float(input("Number: "))
    total += integer
    count += 1

average = total / count
print ()
print ("The average is " + "{:,.1f}".format(average))
