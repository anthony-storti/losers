import data

data.init_db()
cur = data.sqliteConnect()
print(data.fetch(cur, "dummy", "Insults", "date", "insult"))
print(data.fetch(cur, "Rick-Perry"))



