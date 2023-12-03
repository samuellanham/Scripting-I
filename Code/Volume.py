PI = 3.14159

def sphereVolume(radius):
    area = (4/3) * PI * radius * radius * radius
    return area

def main():
    print ("This program computes the volume of a sphere.")
    radius = float(input("Enter the radius: "))
    finalvalue = sphereVolume(radius)
    print ("The volume is", "{:.2f}".format(finalvalue))

main()
