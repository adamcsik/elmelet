import sqlite3

kapcsolat = sqlite3.connect("hallgatok.db")

ab = kapcsolat.cursor()

ab.execute('CREATE TABLE IF NOT EXISTS hallgatok (nev TEXT, email TEXT, neme TEXT)')
"""
ab.execute('INSERT INTO hallgatok VALUES ("Mari", "mari@gmail.com", "nő")')
ab.execute('INSERT INTO hallgatok VALUES ("Teri", "teri@gmail.com", "nő")')
"""
#ab.execute('SELECT nev FROM hallgatok WHERE neme = "nő"')
ab.execute('UPDATE hallgatok SET neme=? WHERE neme=?', ("néni", "nő"))
ab.execute('DELETE FROM hallgatok WHERE neme="férfi"')
ab.execute('SELECT * FROM hallgatok')
adatok = ab.fetchall()
for adat in adatok:
    print(adat)

kapcsolat.commit()
kapcsolat.close()
