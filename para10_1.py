import sqlite3

conection = sqlite3.connect("itstep_DB.sl3", 5)
cur = conection.cursor()
cur.execute("INSERT INTO first_table (name) VALUES ('Vika');")
cur.execute("INSERT INTO first_table (name) VALUES ('Leon');")
cur.execute("INSERT INTO first_table (name) VALUES ('Ydaw');")
conection.commit()
conection.close()

