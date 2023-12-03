print ("This program calculates a letter grade average.")
print ("Enter scores, or -1 to quit.")

print ()
score = float(input("Enter numeric score: "))
summation = 0
count = 0

while (score != -1):
    summation += score
    count += 1
    score = float(input("Enter numeric score: "))

average = summation / count

if (average >= 90):
    print ("Grade: A")
elif (average >= 80):
    print ("Grade: B")
elif (average >= 70):
    print ("Grade: C")
elif (average >= 60):
    print ("Grade: D")
else :
    print ("Grade: F")
