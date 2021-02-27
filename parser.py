import data

cur = data.sqliteConnect()

def command():
    data.init_db()

    # Formats for selecting items on Insults table
    # select date from Insult table by insult example
    print(data.fetch(cur, "dummy", "Insults", "date", "insult"))

    # select insult_id from Insult table by insult example
    print(data.fetch(cur, "dummy", "Insults", "insult_id", "insult"))

    # Formats for selecting items on Losers table
    # select occupation from Losers table by name example
    print(data.fetch(cur, "Rick-Perry", "Losers", "occupation", "name"))

    # select occupation from Losers table by loser_id example
    print(data.fetch(cur, "RP", "Losers", "occupation", "loser_id"))

    # select tweet from Insult table by name example
    print(data.fetch(cur, name))

    # load data example
    insultT, loserT = data.fetchAllQueries(cur)
    print("")
    print("Insults Table")
    print("")
    for insult in insultT:
        print(insult)

    print("")
    print("Losers Table")
    print("")
    for loser in loserT:
        print(loser)

    cur.commit()
    drop_tables()

command()
