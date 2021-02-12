import data
import subprocess
import os
import sys

cur = data.sqliteConnect()

a = sys.argv[1]


def command():
    data.init_db()

    name = str(a)

    print(data.fetch(cur, "dummy", "Insults", "date", "insult"))
    print(data.fetch(cur, name))

    cur.commit()
    drop_tables()


def drop_tables():
    cur.commit()
    cur.close()
    subprocess.call("rm data.db")


command()



