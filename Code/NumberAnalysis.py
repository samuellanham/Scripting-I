print ("Please enter some numbers. Type 'q' to quit.")

number = input("Enter a number: ")
numbers = [number]

while (number != "q"):
    number = input("Enter a number: ")
    if (number != "q"):
        numbers.append(number)

for i in range (len(numbers)):
    numbers[i] = int(numbers[i])

print ("The lowest number is", min(numbers))
print ("The highest number is", max(numbers))
print ("The total of the numbers is", sum(numbers))
print ("The average of the numbers is", "{:,.2f}".format(sum(numbers)/len(numbers)))
