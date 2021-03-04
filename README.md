# CS205 Warm-up Project
> Team 6
### Summary of program
This Program allows a user to query a Sqlite database without using any SQL commands. The data within the database is comprised of two tables. The data is modeled on insults tweeted by former President Donald Trump
The database is comprised of two tables. An insults table and a losers table. 

### Requirements
* The system running this program must have the following:
    * A working copy of Sqlite (for Windows OS: Sqlite must be added as a path variable)
    * Python 3.x
    
### Running the Program
* Before accepting a query the user must enter the command "load data" to initialize the database and flush old data.
* After the data has been initialized the user can begin querying the database of enter "help" to access a list of all available commands and formatting
>The program accepts the following query language:
    - Losers Table Queries
        - To get twitter handle of a particular loser type: Twitter_handle Losers Name 'firstName-lastName' 
        - To get a loser name from their twitter handle type: Name Losers Twitter_handle '@twitterHandle')
        - To get the occupation of a loser type: Occupation Losers Name 'firstName-lastName')
    - Insults Table Queries
        - To get the date of a particular insult type: Date Insults Insult 'insult')
        - To get an insult from a specific date type: Insult Insults Date 'yyyy-mm-dd')
        - To get the full text of a tweet from an insult type: Tweet Insults Insult 'insult')
    - Insult Loser Join Query
        - To get a tweet about a specific Loser type: Tweet Insults Losers 'firstName-LastName')
    - Important Notes about formatting:
        - The query field show in quotations must be entered with quotations in the program
        - Syntax is important. 
            - When entering a name it is important to separate first and last names with a **-**
            - When entering a name the the first letter of both the first and last name must be capitalized
            - Dates must be entered as yyyy-mm-dd
            - The query field is case sensitive 
