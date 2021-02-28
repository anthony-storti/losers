
from parserFunctions import *
import data
import os.path as path

def main():

    keepRunning  = True

    cur = data.sqliteConnect()
    data.init_db()

    print(path.exists("data.db"))

    while keepRunning:
        userInput = input(">")

        if userInput == "quit":
            keepRunning = False
        elif userInput == "help":
            printHelp()



        userInput = inputToList(userInput)

        if validateInput(userInput):
            if len(userInput) == 4:

                if userInput[0] == "tweet" and userInput[1] == "insults" and userInput[2] == "loser_id":
                    print(data.fetch(cur, userInput[3]))

                else:
                    print(data.fetch(cur, userInput[3], userInput[1], userInput[0], userInput[2]))
        else:
            print("Invalid query, type help for list of commands")



main()
