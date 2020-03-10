import sqlite3

conn = sqlite3.connect('Patient_DB.db')
#conn = sqlite3.connect('Login_Details_Database.db')
#conn = sqlite3.connect('Georgios_Zafeiropoulos.db')

cur = conn.cursor()

cur.execute("SELECT * FROM addresses")
#cur.execute("SELECT * FROM users")
#cur.execute("SELECT * FROM records")

var = cur.fetchall()
print(var)

conn.commit()
conn.close()