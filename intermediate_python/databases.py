# https://docs.python.org/3/library/sqlite3.html?highlight=sqlite3#module-sqlite3
import sqlite3

# connets to the database w this name or create new one
connection = sqlite3.connect('mydata.db')
# cursor - to execute sql queries
cursor = connection.cursor()

# from now on its pure sql more or less...
cursor.execute("""
CREATE TABLE IF NOT EXISTS persons (
    id INTEGER PRIMARY KEY,
    first_name VARCHAR(32),
    last_name TEXT,
    age INTEGER
)
""")

cursor.execute("""
INSERT INTO persons VALUES 
(0, 'Paul', 'Smith', 23),
(1, 'Mark', 'Johanson', 41),
(2, 'Anna', 'Smith', 18)
""")

cursor.execute("""
SELECT * FROM persons 
WHERE last_name='Smith'
""")

# to get the results we have to fetch the data:
rows = cursor.fetchall()
print(rows)

connection.commit()

connection.close()
