def half_plus_seven(age):
    minimum = (age / 2) + 7
    return minimum

def main():
    print ("Dating age calculator.")
    num1 = int(input("Enter your age: "))
    print ("Your age is", num1)
    print("Minimum age is", half_plus_seven(num1))

main()
