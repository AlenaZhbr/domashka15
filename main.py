import sqlite3

conn = sqlite3.connect('sql.db')

cur = conn.cursor()

# cur.execute('''CREATE TABLE Pupils(ID PRIMARY KEY NOT NULL, Name TEXT, Surname TEXT)''')

# cur.execute(''' INSERT INTO Pupils(ID, Name, Surname ) VALUES (1, 'Саша', 'Шилкин')''')
# cur.execute(''' INSERT INTO Pupils(ID, Name, Surname ) VALUES (2, 'Саша', 'Шилкин')''')
# cur.execute(''' INSERT INTO Pupils(ID, Name, Surname ) VALUES (3, 'Саша', 'Шилкина')''')

cur.execute('''DELETE FROM Pupils WHERE Surname LIKE '%Шилкин%' ''')

conn.commit()

conn.close()