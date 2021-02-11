import data

data.init_db()
cur = data.sqliteConnect()
print(data.fetch(cur, "Insults", "date", "insult", "dummy"))
print(data.fetch(cur, "Insults", "date", "insult", "dummy", "Loser"))



