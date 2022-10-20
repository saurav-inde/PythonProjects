import mysql.connector as mc

mydb = mc.connect(host="localhost",
                  user="root",
                  password="2050",
                  database="pm")

cursor = mydb.cursor()

cursor.execute("select * from passw")
# cursor.execute("INSERT INTO passw (site, username, password) VALUES" + "('nse.in', 'kite', '3rfcaw')")
# mydb.commit()
for passws in cursor.fetchall():
    print(passws)
