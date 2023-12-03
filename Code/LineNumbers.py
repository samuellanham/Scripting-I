def main():
    filename = input(str("Enter a filename: "))
    
    print()
    
    print ("Contents of", filename)
    contents(filename)

def contents(filename):
    textfile = open(filename, "r")
    line = textfile.readline()
    i = 0
    
    while line != "":
        i += 1
        line = line.rstrip('\n')
        print (i,":", "\t", line, sep = "")
        line = textfile.readline()

    textfile.close()
    
main()
