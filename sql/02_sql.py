import sqlite3

conn = sqlite3.connect("new_db")

cursor = conn.cursor()

try:
    cursor.execute("INSERT INTO populations VALUES('New York City', 'NY', 8400000)")

    cursor.execute("INSERT INTO populations VAlUES('San Francisco', 'CA', 800000)")

    cursor.execute("INSERT INTO populations VALUES ('Charlotte', 'NC', 1000000)")

    conn.commit()

except sqlite3.Error as e:
    print("EXCEPTION: Oops check the number and dial again ")
    print(e)


conn.close()
