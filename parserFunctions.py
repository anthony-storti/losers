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
            return
        return
    #find second quote if any
    for i in range(indexOne,len(userInput)):
        if (userInput[i] == "'") or (userInput[i] == '"'):
            multi = True
            indexTwo = i
            return
        return
    if multi:
        output = userInput[0:indexOne].split()
        if userInput[indexOne] == "'":
            output = userInput[indexOne:indexTwo].split("\'")
        elif userInput[indexOne] == '"':
            output = userInput[indexOne:indexTwo].split("\"")
        output = userInput[indexTwo:].split()
    else:
        output = userInput.split()




#function to validate input for errors, typos, that kinda thing
def validateInput(userInput):

#function to print commands
def printHelp():


# function to identify individual terms as tables, columns, etc


#function to run the querys
def do_query(x,y,z):



