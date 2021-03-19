import sqlite3
import requests

conn=sqlite3.connect('dati.db')
c=conn.cursor()

c.execute('PRAGMA foreign_keys=ON')
c.execute('CREATE TABLE IF NOT EXISTS laiks (laiks_id INTEGER PRIMARY KEY AUTOINCREMENT, laiki TEXT)')
c.execute('CREATE TABLE IF NOT EXISTS audzinatajs (audzinataja_id INTEGER PRIMARY KEY AUTOINCREMENT, klases_id INTEGER, pasniedzeja_id INTEGER)')
c.execute('CREATE TABLE IF NOT EXISTS prieksmeti (prieksmeta_id INTEGER PRIMARY KEY  AUTOINCREMENT  , prieksmets TEXT)')
c.execute('CREATE TABLE IF NOT EXISTS dienas (dienas_id INTEGER PRIMARY KEY AUTOINCREMENT, diena TEXT)')
c.execute('CREATE TABLE IF NOT EXISTS pasniedzejs (pasniedzeja_id INTEGER PRIMARY KEY AUTOINCREMENT , vards TEXT, uzvards TEXT, epasts TEXT,telefons TEXT, prieksmeta_id INTEGER,FOREIGN KEY(prieksmeta_id) REFERENCES prieksmeti(prieksmeta_id))')
c.execute('CREATE TABLE IF NOT EXISTS klases (klases_id INTEGER PRIMARY KEY AUTOINCREMENT  , klase TEXT)')
c.execute('CREATE TABLE IF NOT EXISTS stundas (stundas_id INTEGER PRIMARY KEY AUTOINCREMENT , dienas_id INTEGER, klases_id INTEGER,prieksmeta_id INTEGER,pasniedzeja_id INTEGER,laiks_id INTEGER,notiek INTEGER)')
#c.execute('INSERT INTO audzinatajs(klases_id, pasniedzeja_id) VALUES (1,1),(2,2),(3,3)')

#c.execute('INSERT INTO dienas (diena) VALUES ("Pirmdiena"),("Otrdiena"),("Trešdiena"),("Ceturtdiena"),("Piektdiena")')
#c.execute('INSERT INTO laiks (laiki) VALUES ("7:45-8:25"),("8:30-9:10"),("9:15-9:55"),("10:15-10:55"),("11:20-12:05"),("12:35-13:05"),("13:20-14:00"),("14:05-14:45"),("14:50-15:30")')
#c.execute('INSERT INTO prieksmeti (prieksmets) VALUES("Angļu valoda"),("Bioloģija"),("Dabaszinības"),("Ekonomika"),("Fizika"),("Franču valoa"),("Ģeogrāfija"),("Grāmatvedība"),("Informātika"),("Ķīmija"),("Klases stunda"),("Krievu valoda"),("Kulturoloģija"),("Latviešu valoda"),("Literatūra"),("Mājturība un tehnoloģijas"),("Matemātika"),("Mūzika"),("Programmēšanas pamati"),("Projektu vadība"),("Sociālās zinības"),("Sports"),("Vācu valoda"),("Vizuālā māksla"),("Pasaules vēsture"),("Drāma"),("Dizains un tehnoloģijas")')
#c.execute('INSERT INTO pasniedzejs (vards,uzvards,epasts,telefons,prieksmeta_id) VALUES("Andris","Bērziņš","andris.berzins@gmail.com","26752897",25),("Pēteris","Skuja","peteris.skuja@gmail.com","26865415",22),("Anna","Panna","anna.panna@gmail.com","26444321",4),("Valdis","Liepa","valdis.liepa@gmail.com","26865415",17),("Elita","Bērziņa","elita.berzina@gmail.com","26753159",16),("Andra","Saule","andra.saule@gmail.com","265488784",1);')

#c.execute('INSERT INTO klases (klase) VALUES ("1.a"),("1.b"),("1.c"),("2.a"),("2.b"),("2.c"),("3.a"),("3.b"),("3.c"),("4.a"),("4.b"),("4.c"),("5.a"),("5.b"),("5.c"),("6.a"),("6.b"),("6.c"),("7.a"),("7.b"),("7.c"),("8.a"),("8.b"),("8.c"),("9.a"),("9.b"),("9.c"),("10.a"),("10.b"),("10.c"),("9.c"),("10.a"),("10.b"),("10.c"),("11.a"),("11.b"),("11.c"),("12.a"),("12.b"),("12.c")')

#c.execute('INSERT INTO stundas (dienas_id,klases_id,prieksmeta_id,pasniedzeja_id,laiks_id,notiek) VALUES(1,1,23,1,1,1),(1,1,20,8,2,1),(1,1,25,3,3,1),(1,1,11,7,4,1),(1,1,2,4,5,1),(2,1,24,5,1,1),(2,1,21,5,2,1),(2,1,2,2,3,1),(2,1,23,4,4,1),(2,1,6,3,6,1),(3,1,22,6,1,1),(3,1,7,2,2,1),(3,1,4,3,3,1),(3,1,24,4,4,1),(4,1,3,4,1,1),(4,1,8,5,2,1),(4,1,26,3,3,1),(4,1,3,7,4,1),(5,1,12,5,2,1),(5,1,25,5,3,1),(5,1,11,2,4,1),(1,2,23,2,1,1),(1,2,22,8,2,1),(1,2,7,8,3,1),(1,2,4,6,4,1),(1,2,23,8,5,1),(2,2,5,7,1,1),(2,2,18,4,3,1),(2,2,9,8,4,1),(2,2,10,2,5,1),(2,2,10,8,6,1),(3,2,22,3,1,1),(3,2,3,4,2,1),(3,2,24,1,3,1),(3,2,13,6,4,1),(4,2,24,2,1,1),(4,2,23,3,3,1),(4,2,24,1,4,1),(5,2,23,6,1,1),(5,2,12,7,2,1),(5,2,14,7,3,1),(5,2,17,1,4,1),(1,3,26,3,1,1),(1,3,16,2,2,1),(1,3,14,3,3,1),(1,3,12,2,5,1),(2,3,2,7,1,1),(2,3,22,4,2,1),(2,3,18,7,3,1),(2,3,20,4,4,1),(2,3,15,6,5,1),(2,3,22,5,6,1),(3,3,12,5,1,1),(3,3,21,3,2,1),(3,3,8,8,4,1),(4,3,15,5,1,1),(4,3,22,4,2,1),(4,3,24,3,3,1),(4,3,16,8,4,1),(5,3,22,1,1,1),(5,3,10,7,2,1),(5,3,1,7,3,1),(5,3,1,7,4,1)')

#c.execute('INSERT INTO pasniedzejs (vards,uzvards,epasts,telefons,prieksmeta_id) VALUES("Marta","Kalniņa","marta.kalnina@gmail.com","24343545",15),("Pēteris","Ozols","peteris.ozolsa@gmail.com","268344315",27);')
#c.execute("SELECT * FROM stundas ")
#print(c.fetchall())

#c.execute("SELECT * FROM stundas")
#print(c.fetchall())

#c.execute("SELECT stundas_id, prieksmeti.prieksmets, pasniedzejs.vards FROM stundas JOIN prieksmeti ON stundas.prieksmeta_id = prieksmeti.prieksmeta_id JOIN PASNIEDZEJS ON stundas.pasniedzeja_id=pasniedzejs.pasniedzeja_id")
#c.execute("SELECT  pasniedzejs.vards, pasniedzejs.uzvards, pasniedzejs.epasts, pasniedzejs.telefons, prieksmeti.prieksmets FROM pasniedzejs JOIN prieksmeti ON pasniedzejs.prieksmeta_id = prieksmeti.prieksmeta_id ")
#c.execute('INSERT INTO audzinatajs(klases_id, pasniedzeja_id) VALUES (8,8)')
#c.execute("SELECT  dienas.dienas_id,laiks.laiks_id,klases.klase,prieksmeti.prieksmets, pasniedzejs.vards, pasniedzejs.uzvards, laiks.laiki, stundas.notiek FROM stundas JOIN dienas ON stundas.dienas_id = dienas.dienas_id JOIN laiks ON stundas.laiks_id = laiks.laiks_id JOIN prieksmeti ON stundas.prieksmeta_id = prieksmeti.prieksmeta_id JOIN pasniedzejs ON stundas.pasniedzeja_id = pasniedzejs.pasniedzeja_id JOIN klases ON stundas.klases_id = klases.klases_id  ")
c.execute("SELECT klases.klase,prieksmeti.prieksmets,laiks.laiki,stundas.dienas_id FROM stundas JOIN dienas ON stundas.dienas_id = dienas.dienas_id JOIN laiks ON stundas.laiks_id = laiks.laiks_id JOIN prieksmeti ON stundas.prieksmeta_id = prieksmeti.prieksmeta_id  JOIN klases ON stundas.klases_id = klases.klases_id  WHERE  klases.klase LIKE '1.c'")
rows = c.fetchall()

for row in rows:
    print(row)
# print(c.fetchall())
conn.commit()
c.close()
conn.close()
