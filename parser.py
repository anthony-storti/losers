import data

data.init_db()
cur = data.sqliteConnect()
print(data.fetch(cur, "Insults", "date", "insult", "weak"))




