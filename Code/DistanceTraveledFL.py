speed = int(input("What is the speed of the vehicle in mph? "))
hours = int(input("How many hours has it traveled? "))

print ("Hour    Distance Traveled")
print ("-------------------------")

for x in range (1, hours + 1):
    print (x, "     ", speed * x)
