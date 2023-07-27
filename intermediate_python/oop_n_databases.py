import sqlite3


# the database should  to already exist - how to create see databases.py

class Person:
    def __init__(self, id_num=-1, firs="", last="", age=-1):
        self.id_num = id_num
        self.first = firs
        self.last = last
        self.age = age
        # connets to the database w this name or create new one
        self.connection = sqlite3.connect('mydata.db')
        # cursor - to execute sql queries
        self.cursor = self.connection.cursor()

    def load_person(self, id_num):
        self.cursor.execute("""
        SELECT * FROM persons
        WHERE id = {}
        """.format(id_num))

        result = self.cursor.fetchone()  # - only unique
        self.id_num = id_num
        self.first = result[1]
        self.last = result[2]
        self.age = result[3]

    def insert_person(self):
        # watchout, when string need to specify with: '{}'
        self.cursor.execute("""
        INSERT INTO persons VALUES 
        ({}, '{}', '{}', {})
        """.format(self.id_num, self.first, self.last, self.age))

        self.connection.commit()


p1 = Person()
p1.load_person(1)
print(p1.first, p1.last, p1.age, p1.id_num)


p2 = Person(7, "Alex", "Robbins", 30)
p2.insert_person()

conn = sqlite3.connect('mydata.db')
curs = conn.cursor()

curs.execute("SELECT * FROM persons")
results = curs.fetchall()
print(results)
conn.close()

