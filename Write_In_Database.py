import sqlite3

#conn = sqlite3.connect("C:/Users/Georgios/PycharmProjects/Patient_Registration_System/Patient_Medical_Records/Nick_Smith.db")
conn = sqlite3.connect("C:/Users/zafir/PycharmProjects/Patient_Registration_System/Patient_Medical_Records/Nick_Smith.db")

cur = conn.cursor()
'''cur.execute("""CREATE TABLE IF NOT EXISTS pat_med_rec (
                                    medrec_id integer PRIMARY KEY NOT NULL,
                                    pat_id text NOT NULL,
                                    pat_name text NOT NULL,
                                    date text NOT NULL,
                                    notes text NOT NULL,
                                    added text NOT NULL
                            )""")'''

patient_id = """INSERT INTO pat_med_rec (pat_id, pat_name, date, notes, added) VALUES (?, ?, ?, ?, ?) """

id_pat = 2
name = 'Nick Smith'
datenow = '2020-02-05'
notetext = 'Duis eget sem id ipsum elementum fermentum. Etiam pharetra nunc quis velit interdum luctus. Morbi a ' \
           'iaculis purus. Quisque non blandit massa. Duis porttitor condimentum erat, eget mollis dui pulvinar non. ' \
           'Nullam at volutpat justo, eleifend pulvinar turpis. Donec nec pharetra magna, eu convallis risus. ' \
           'Maecenas et fermentum magna. Vivamus ultrices, libero quis vestibulum volutpat, nulla mauris volutpat ' \
           'elit, eu facilisis lectus massa eget diam. Curabitur at arcu eu dui posuere faucibus. Fusce mauris dolor, ' \
           'pretium nec felis eget, condimentum efficitur nibh. Nulla facilisi. '
addedby = 'Zafeiropoulos'
cur.execute(patient_id, (id_pat, name, datenow, notetext, addedby))


cur.execute('''SELECT * from pat_med_rec''')
print(cur.fetchall())

conn.commit()
conn.close()