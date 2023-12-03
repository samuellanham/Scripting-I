print ("This program calculates area or volume.")
formula = str(input("Would you like to calculate area or volume? "))

print()

if (formula == "area"):
    shape = str(input("Would you like to calculate the area of a triangle or a circle? "))
    if (shape == "triangle"):
        base = float(input("Enter the base: "))
        height = float(input("Enter the height: "))
        area = (base * height)/2
        print ("The area is", "{:.2f}".format(area))
    elif (shape == "circle"):
        radius = float(input("Enter the radius: "))
        area = 3.14 * (radius * radius)
        print ("The area is", "{:.2f}".format(area))
    else :
        print ("Invalid input.")
elif (formula == "volume"):
    shape = str(input("Would you like to calculate the volume of a cylinder or a sphere? "))
    if (shape == "cylinder"):
        height = float(input("Enter the height: "))
        radius = float(input("Enter the radius: "))
        volume = 3.14 * (radius * radius) * height
        print ("The volume is", "{:.2f}".format(volume))
    elif (shape == "sphere"):
        radius = float(input("Enter the radius: "))
        volume = (4/3) * 3.14 * (radius * radius * radius)
        print ("The volume is", "{:.2f}".format(volume))
    else :
        print ("Invalid input.")
else :
    print ("Invalid input.")
    
