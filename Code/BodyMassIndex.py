def BMI_Calculate(weight, height):
    BMI = ((weight * 703)/(height * height))
    return (BMI)

weight = int(input("Enter the weight: "))
height = int(input("Enter the height: "))
finalvalue = BMI_Calculate(weight, height)

print ("Body Mass Indicator:", "{:,.2f}".format(finalvalue))
