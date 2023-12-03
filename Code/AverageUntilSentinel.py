print ("This program averages numbers.")
number = 0.0
summation = 0.0
count = -1

while (number >= 0.0):
    summation += number
    number = float(input("Number: "))
    count += 1

average = summation / count

print()
print ("The average is", "{:,.2f}".format(average))
