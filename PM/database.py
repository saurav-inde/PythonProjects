import mysql.connector as mc


class database:
    def __init__(self, pm = None):
        self.mydb = self.make_connection(pm)
        self.cursor = self.mydb.cursor()

    def make_connection(self, pm):
        # return mc.connect(
        #     host=pm.user["host"],
        #     user=pm.user["username"],
        #     password=pm.user["password"]
        # )
        return mc.connect(
            host="localhost",
            user="root",
            password="2050",
            database = "pm"
        )

    def execute(self, command):
        self.cursor.execute(command)
        # return q_result
    # def insert(self):

if __name__ == "__main__":
    db = database()
    db.cursor.execute("SHOW databases")
    db.cursor.execute("use pm")
    # a = db.cursor.execute("SELECT * FROM passw")
    print(db.cursor.fetchall())
