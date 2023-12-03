def letterPick (textLine):
    newLine = textLine[0] + textLine[4] + textLine[7] + textLine[12] + textLine[20]

    return newLine

def main ():
    textLine = str(input("Enter a line of text: "))

    print ("Message:", letterPick(textLine))

main()
