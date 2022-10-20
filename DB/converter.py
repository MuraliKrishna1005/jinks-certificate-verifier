#Import required files
import sqlite3
import pandas as pd

#connect to sql db
converter_con = sqlite3.connect("DB/jinks23.sql", check_same_thread=False)
cur = converter_con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Institute TEXT, Event TEXT, UNIQUE (Name, Institute, Event))")
converter_con.commit()

# Load the xlsx file
data = pd.read_excel('DB/Participants.xlsx')

#Insert Rows of xlsx to db
for i in data.index:
    try:
        cur.execute(f"""INSERT INTO student(Name, Institute, Event) VALUES('{data['Name'][i]}','{data['Institute'][i]}','{data['Event'][i]}')""")
    except sqlite3.IntegrityError:
        pass #Pass all Already existing Recordds
    except:
        print("error")
converter_con.commit()

#Display the final DB
for row in cur.execute("SELECT * FROM student"):
    print(row)