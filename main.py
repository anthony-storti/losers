
from parserFunctions import inputToList
from parserFunctions import validateInput
def main():



    string = "heyo this is a test of a 'magnificient function'"
    test = inputToList(string)
    print(test)
    print(test[7])




    # validation function testing
    regularTestTrue = ["Date", "Insults", "insult", "Search term"]
    regularTestFalse = ["Date", "Insult", "insult", "search"]
    tooSmall = ["not", "enough"]
    tooBig = ["too", "many", "terms", "in", "list"]


    # true
    print(validateInput(regularTestTrue))

    # false
    print(validateInput(regularTestFalse))

    # false
    print(validateInput(tooSmall))

    # false
    print(validateInput(tooBig))


main()
