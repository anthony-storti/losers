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



# function to validate input for errors, typos, that kinda thing
# designed to take in a list of 3 or 4 string components: column, table, (table 2 for join), and search term
# returns true if the userInput is valid, false otherwise
def validateInput(userInput):
    isValid = False
    column = userInput[0].lower()
    table = userInput[1].lower()
    insultTableColumns = ["insult_id", "tweet", "date", "insult", "loser_id"]
    loserTableColumns = ["loser_id", "name", "twitter_handle", "occupation"]
    tableNames = ["loser", "insult"]

    # check whether 3 (regular statement) or 4 (join statement) items are in the list
    # validate regular statement
    if len(userInput) == 3:
        # if insult table was selected, check if column is valid
        if table == "insult":
            if column in insultTableColumns:
                isValid = True

        # if Loser table was selected, check if columns are valid
        if table == "loser":
            if column in loserTableColumns:
                isValid = True

    # validate join statement
    elif len(userInput) == 4:
        # get the 2nd table name
        tableTwo = userInput[2].lower()
        # check that both the tables and the
        if table in tableNames and tableTwo in tableNames:
            if column in insultTableColumns or column in loserTableColumns:
                isValid = True

    # otherwise the input list is too long or too short, return false
    else:
        return isValid

    return isValid






#function to print commands
#def printHelp():


# function to identify individual terms as tables, columns, etc


#function to run the querys
#def do_query(x,y,z):



