mapping = ["ABC","DEF","GHI","JKL","MNO", "PQRS", "TUV", "WXYZ"]

def letToNum(letter):
    for i,group in enumerate(mapping):
        if letter.upper() in group:
            return str(i+2)
        #else:
    return letter
    
def convertNum(string_input):
    numNumber = ""
    for x in string_input:
        if x.isalpha():
            numNumber += letToNum(x)
        else:
            numNumber += x
    numNumber += "."
    
    return numNumber
        
finalNumber = convertNum(input("Please enter an alphabetic telephone number:"))

print("The converted telephone number is", finalNumber)
