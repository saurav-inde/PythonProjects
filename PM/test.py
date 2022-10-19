import mysql.connector as mc

mydb = mc.connect(host="localhost",
                  user="root",
                  password="2050",
                  database="pm")

cursor = mydb.cursor()

cursor.execute("select * from passw")
print(cursor.fetchall())
