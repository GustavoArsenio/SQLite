import sqlite3

CONNECTION = sqlite3.connect('test.db')
cursor = CONNECTION.cursor()

for row in cursor.execute('SELECT * FROM meu_teste'):
    print(row)

CONNECTION.commit()
CONNECTION.close()
