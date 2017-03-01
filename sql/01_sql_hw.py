import  sqlite3

conn2 = sqlite3.connect("new_db")

cursor = conn2.cursor()

cursor.execute("""CREATE TABLE cars (Make TEXT, model TEXT, year INT, quantity INT) """)

cursor.close()