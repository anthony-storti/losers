import sqlite3
# function to take a string input and break it up into a list of components, being mindful of quotation marks

def inputToList(userInput):
    userInput = userInput.lower()
    output = []
    indexOne = 0
    indexTwo = 0
    multi = False
    #find first quote if any
    for i in range(len(userInput)):
        if (userInput[i] == "'") or (userInput[i] == '"'):
            multi = True
            indexOne = i
            break

    #find second quote if any
    for j in range(indexOne+1, len(userInput)):
        if (userInput[j] == "'") or (userInput[j] == '"'):
            indexTwo = j
            break

    if multi:
        output = userInput[0:indexOne].split()
        if userInput[indexOne] == "'":
            output += userInput[indexOne:indexTwo].split("'")
        elif userInput[indexOne] == '"':
            output += userInput[indexOne+1:indexTwo].split('"')
        output += userInput[indexTwo:].split()
    else:
        output += userInput.split()

    return output




