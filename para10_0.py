import sqlite3

conection = sqlite3.connect("itstep_DB.sl3", 5)
cur = conection.cursor()
cur.execute("SELECT rowid, name FROM first_table VALUES ('Vasya');")
res = cur.fetchall()
print(res)
conection.close()
