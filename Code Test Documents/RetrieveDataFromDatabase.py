import sqlite3

conn = sqlite3.connect("C:/Users/Georgios/PycharmProjects/Patient_Registration_System/Patient_Medical_Records/John_Smith.db")
cur = conn.cursor()
#=========This is to return dates===================
'''validMonth = False
while not validMonth:
    lookForMonth = input('Which months data? (Enter 1 to 12): ')
    try:
        validMonth = 1<=int(lookForMonth)<=12
    except:
        pass

sqlCmd = 'SELECT date from pat_med_rec WHERE SUBSTR(date,4,2)="%.2i"' % int(lookForMonth)
for row in conn.execute(sqlCmd):
    print(row)'''

# ====================This is to return everything based on a date ==========================
'''dates = '%%/%%/2020'
cur.execute("SELECT * from pat_med_rec WHERE date LIKE '%%/%%/2019'")
alpha = cur.fetchall()
print(dates)
print(alpha)'''

#===================This is to return dates but all in one list================
'''lookForMonth = '1'
cur.execute('SELECT date from pat_med_rec WHERE SUBSTR(date,4,2)="%.2i"' % int(lookForMonth))
alpha = cur.fetchall()
print(alpha)'''


test = '2020-01-%%'
cur.execute("SELECT * FROM pat_med_rec WHERE date > ?", (test,))
alpha = cur.fetchall()
print(alpha)



conn.commit()
conn.close()