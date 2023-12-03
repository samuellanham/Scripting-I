print ("This program displays numbers read from a file.")

display = open("numbers.txt", "r")
lines = display.readlines()

for i in range (len(lines)):
    print ("Number:", int(lines[i]))
    
display.close()
