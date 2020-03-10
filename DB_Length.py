import sqlite3

conn = sqlite3.connect('Test.db')

cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS addresses (
                    first_name text,
                    last_name text,
                    address text,
                    postcode text,
                    city text,
                    mobile text,
                    email txt,
                    DoB text,
                    gender text,
                    PatID text
            )""")

cur.execute("SELECT * FROM addresses")
var = cur.fetchall()
print(var)
if len(var) == 0:
    print("It's empty")
else:
    print(len(var))

'''pid = str(len(var) + 1)
cur.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :addr, :post, :city, :mob, :email, :dob, :gnd, :patid)",
                    {
                        'f_name': 'Georgios',
                        'l_name': 'Zafeiropoulos',
                        'addr': '171 Farringdon Road',
                        'post': 'EC1R 3AL',
                        'city': 'London',
                        'mob': '07784625831',
                        'email': 'giorgos785@gmail.com',
                        'dob': '12-07-1985',
                        'gnd': 'Male',
                        'patid': pid
                    })


cur.execute("SELECT * FROM addresses")
var = cur.fetchall()
#print(len(var))
if len(var) == 0:
    print("It's empty")
else:
    print(len(var))'''

conn.commit()
conn.close()
