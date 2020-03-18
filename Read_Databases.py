import sqlite3

#conn = sqlite3.connect('Patient_DB.db')
#conn = sqlite3.connect('Login_Details_Database.db')
#conn = sqlite3.connect('Georgios_Zafeiropoulos.db')
conn = sqlite3.connect("C:/Users/Georgios/PycharmProjects/Patient_Registration_System/Patient_Medical_Records/Nick_Smith.db")
#conn = sqlite3.connect("C:/Users/Georgios/PycharmProjects/Patient_Registration_System/Patient_Medical_Records/John_Smith.db")

cur = conn.cursor()

#cur.execute("SELECT * FROM patients")
#cur.execute("SELECT * FROM users")
#cur.execute("SELECT * FROM records")
cur.execute("SELECT * FROM pat_med_rec")


var = cur.fetchall()
print(var)

conn.commit()
conn.close()