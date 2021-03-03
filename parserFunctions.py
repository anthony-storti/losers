import sqlite3
# function to take a string input and break it up into a list of components, being mindful of quotation marks

def inputToList(userInput):
    #userInput = userInput.lower()
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
# returns true if the userInput is valid, false otherwise
def validateInput(userInput):
    isValid = False
    insultTableColumns = ["insult_id", "tweet", "date", "insult", "loser_id"]
    loserTableColumns = ["loser_id", "name", "twitter_handle", "occupation"]

    # check to make sure input list has right number of components
    if len(userInput) == 4:
        # get list components
        column = userInput[0].lower()
        table = userInput[1].lower()
        id = userInput[2].lower()

        # if Insults table was selected, check if column and id are valid, additional check for join statement
        if table == "insults":
            if column in insultTableColumns and id in insultTableColumns or id == "losers":
                isValid = True

        # if Losers table was selected, check if column and id are valid
        if table == "losers":
            if column in loserTableColumns and id in loserTableColumns:
                isValid = True

    # if only 2 terms are given, check if it's the load data command
    elif len(userInput) == 2 and userInput[0].lower() == "load" and userInput[1].lower() == "data":
        isValid = True

    # otherwise the input list is too long or too short, return false
    else:
        return isValid

    return isValid


#function to print commands
def printHelp():
    print("You can type the following types of commands with this interface:")
    print("Anything in 'quotes' should by input with the quotation marks!")
    print("Information about Losers:")
    print("To get twitter handle of a particular loser: Twitter_handle Losers Name 'Rick-Perry'")
    print("To get a name from a handle simply switch the two terms: Name Losers Twitter_handle '@GovernorPerry'")
    print("Information about individual Insults:")
    print("To learn the date of an insult: Date Insults Insult 'dummy'")
    print("To get an insult from a specific date: Insult Insults Date '2015-07-16")
    print("to get the full text of a tweet from an insult: Tweet Insults Insult 'boring guy'")
    print("Misc other:")
    print("To perform a join statement about a specific loser: Tweet Insults Losers 'Rick-Perry'")

# function to identify individual terms as tables, columns, etc


#function to run the querys
#def do_query(x,y,z):



