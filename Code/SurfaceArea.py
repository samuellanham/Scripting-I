PI = 3.14159

def sphereArea(radius):
    area = 4 * PI * radius * radius
    return area

def main():
    print ("This program computes the surface area of a sphere.")
    radius = float(input("Enter the radius: "))
    finalvalue = sphereArea(radius)
    print ("The surface area is", "{:.2f}".format(finalvalue))

main()
