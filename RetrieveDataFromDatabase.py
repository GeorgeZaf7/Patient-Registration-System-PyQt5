import sqlite3

conn = sqlite3.connect("C:/Users/Georgios/PycharmProjects/Patient_Registration_System/Patient_Medical_Records/Nick_Smith.db")
cur = conn.cursor()

validMonth = False
while not validMonth:
    lookForMonth = input('Which months data? (Enter 1 to 12): ')
    try:
        validMonth = 1<=int(lookForMonth)<=12
    except:
        pass

sqlCmd = 'SELECT date from pat_med_rec WHERE SUBSTR(date,4,2)="%.2i"' % int(lookForMonth)
for row in conn.execute(sqlCmd):
    print(row)

conn.commit()
conn.close()