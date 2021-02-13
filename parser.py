import data
import subprocess
import os
import sys

cur = data.sqliteConnect()

a = sys.argv[1]


def command():
    data.init_db()

    name = str(a)

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
    rows = data.fetchAllQueries(cur)
    for row in rows:
        print(row)

    cur.commit()
    drop_tables()


def drop_tables():
    cur.commit()
    cur.close()
    subprocess.call("rm data.db")


command()
