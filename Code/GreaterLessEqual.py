print ("This program reads in two ints and determines if they are equal.")

int1 = int(input("Int 1: "))
int2 = int(input("Int 2: "))

if (int1 < int2):
    print(int1, "is less than", int2)
elif (int1 > int2):
    print(int1, "is greater than", int2)
else :
    print(int1, "is equal to", int2)
