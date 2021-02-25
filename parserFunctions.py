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
            output += userInput[indexOne+1:indexTwo].split("'")
        elif userInput[indexOne] == '"':
            output += userInput[indexOne+1:indexTwo].split('"')
        output += userInput[indexTwo:len(userInput)-1].split()
    else:
        output += userInput.split()

    return output



# function to validate input for errors, typos, that kinda thing
# designed to take in a list of 4 string components: column, table, ID, and search term,
# or just 1 term in the case of a join statement query
# returns true if the userInput is valid, false otherwise
def validateInput(userInput):
    isValid = False
    insultTableColumns = ["insult_id", "tweet", "date", "insult", "loser_id"]
    loserTableColumns = ["loser_id", "name", "twitter_handle", "occupation"]
    tableNames = ["Losers", "Insults"]

    # check to make sure input list has right number of components
    if len(userInput) == 4:
        # get list components
        column = userInput[0].lower()
        table = userInput[1]
        id = userInput[2].lower()

        # if Insults table was selected, check if column and id are valid
        if table == "Insults":
            if column in insultTableColumns and id in insultTableColumns:
                isValid = True

        # if Losers table was selected, check if column and id are valid
        if table == "Losers":
            if column in loserTableColumns and id in loserTableColumns:
                isValid = True

    # validate join statement
    elif len(userInput) == 1:
        # only one term was given (search term) for join statement
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



