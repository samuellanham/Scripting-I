def main():
    print ("This program averages numbers inside a given file.")

    filename = input(str("Enter a filename: "))
    while (filename != "quit"):
        print ("The average is", "{:.2f}".format(math(filename)))
        filename = input(str("Enter a filename: "))

def math(filename):
    textfile = open(filename, "r")
    lines = textfile.readlines()
    total = 0
    count = 0
    
    for i in range (len(lines)):
        total += int(lines[i])
        count += 1
        
    average = total/count
    textfile.close()
    
    return average

main()
