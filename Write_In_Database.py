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

cur.execute(patient_id,
            ('3', 'Nick Smith', '05/01/2020', 'Test test test test test test'))
conn.commit()
conn.close()