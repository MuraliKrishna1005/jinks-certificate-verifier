import sqlite3

#connect to sql db
check_con = sqlite3.connect("DB/jinks23.sql", check_same_thread=False)
cur = check_con.cursor()

def checker(id):
    cur.execute(f"""
    SELECT * 
    FROM student
    WHERE id='{id}'""")
    row = cur.fetchall()
    if len(row)>=1:
        return True
    else:
        return False

def data(id):
    cur.execute(f"""
    SELECT Name, Institute, Event
    FROM student
    WHERE id='{id}'""")
    row = cur.fetchone()
    return row