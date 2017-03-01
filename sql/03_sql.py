import sqlite3

with sqlite3.connect("new_db") as connection:
    cursor = connection.cursor()

cities = [('Rock Hill', 'SC', 1000000),
          ('Boston', 'MA', 600000),
          ('Houston', 'TX', 2100000),
          ('Chicago', 'IL', 2700000),
          ('Phoenix', 'AZ', 1500000)

]

cursor.executemany('INSERT INTO population VALUES(?, ?, ?)', cities)
