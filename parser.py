import data
connection = data.sqliteConnect()
data_tuple = (1, "John Smith", "John-Smith64", "Truck Driver")
data.flushDb(connection)




