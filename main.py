
from parserFunctions import inputToList
from parserFunctions import validateInput
def main():



    string = "heyo this is a test of a 'magnificient function'"
    print(inputToList(string))



    # validation function testing
    regularTestTrue = ["Date", "insult", "Search term"]
    regularTestFalse = ["bobdole", "insult", "search"]
    tooSmall = ["not", "enough"]
    tooBig = ["way", "too", "long", "filler", "words"]
    joinTestTrue = ["tweet", "insult", "loser", "search"]
    joinTestFalse = ["insult", "tweet", "loser", "search"]

    # true
    print(validateInput(regularTestTrue))

    # false
    print(validateInput(regularTestFalse))

    # false
    print(validateInput(tooBig))

    # false
    print(validateInput(tooSmall))

    # true
    print(validateInput(joinTestTrue))

    # false
    print(validateInput(joinTestFalse))

main()
