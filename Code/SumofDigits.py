def addition (inputNumber):
    total = 0
    
    for i in range (len(inputNumber)):
        total += int(inputNumber[i])

    return str(total)

def main():
    print ("This program adds together numbers.")
    inputNumber = str(input("Please enter a string of numbers:"))
    print ("The sum of these digits is " + addition(inputNumber) + ".")

main()
