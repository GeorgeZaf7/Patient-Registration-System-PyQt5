import sqlite3

conn = sqlite3.connect("C:/Users/Georgios/PycharmProjects/Patient_Registration_System/Patient_Medical_Records/Nick_Smith.db")
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS pat_med_rec (
                                    medrec_id integer PRIMARY KEY NOT NULL,
                                    pat_id text NOT NULL,
                                    pat_name text NOT NULL,
                                    date text NOT NULL,
                                    notes text NOT NULL
                            )""")

patient_id = """INSERT INTO pat_med_rec (pat_id, pat_name, date, notes) VALUES (?, ?, ?, ?) """

id_pat = 3
name = 'Nick Smith'
datenow = '2019-10-13'
notetext = 'Test test test test test test'
cur.execute(patient_id, (id_pat, name, datenow, notetext))


cur.execute('''SELECT * from pat_med_rec''')
print(cur.fetchall())

conn.commit()
conn.close()