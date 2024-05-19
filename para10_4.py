import sqlite3

conection = sqlite3.connect("itstep_DB.sl3", 5)
cur = conection.cursor()
cur.execute("CREATE TABLE first_table (name, TEXT);")
conection.commit()
conection.close()
