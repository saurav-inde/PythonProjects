import sqlite3


class Database:
    def __init__(self):
        self.mydb = sqlite3.connect("data.db")

        self.cursor = self.mydb.cursor()
        table = "CREATE TABLE IF NOT EXISTS passw (site varchar(255), " \
                "username varchar(255), password varchar(255)," \
                "ID INTEGER PRIMARY KEY AUTOINCREMENT)"
        self.execute(command=table, commit=True)

    def execute(self, command, commit=False):
        # print("command executed =", command, end="\n")
        self.cursor.execute(command)
        if commit:
            self.mydb.commit()

# if __name__ == "__main__":
#     from  aes import AESCipher
#
#     key = input("Enter masterkey: ")
#     cipher = AESCipher(key)
#
#     db = database()
#     # db.cursor.execute("SHOW databases")
#     # db.cursor.execute("use pm")
#     a = db.cursor.execute("SELECT * FROM passw")
#     for iter in db.cursor.fetchall():
#         print(iter[0],iter[1],cipher.decrypt(iter[2]),iter[3])
