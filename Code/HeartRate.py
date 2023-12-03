def THR(age, restRate):
    maxhr = 220 - age
    traininghr = maxhr - restRate
    traininghr *= 0.60
    traininghr += restRate
    return (traininghr)

age = int(input("Enter your age: "))
restinghr = int(input("Enter your resting heart rate: "))

finalvalue = THR (age, restinghr)
print ("Your training heart rate is:", "{:,.2f}".format(finalvalue))
