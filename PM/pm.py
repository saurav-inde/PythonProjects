import sys
from password import password
from database import database


class PM:
    def __init__(self):

        self.database = database(self)
        self.user ={"host" : "localhost",
                    "password" : "2050",
                    "username" : "root",
                    "database" : "PM"
                    }
        self.authaucticated = 0
        self.auth()
        if not self.authaucticated:
            sys.exit()
        self.passw = password(self)
        self.passw.menu()
    def auth(self):
        mk = input("Enter the masterkey: ")
        masterkey = "332211"
        if mk == masterkey:
            self.authaucticated = 1


    def delete(self, password):
        
        pass
    def update(self, new_password):
        pass
        # self.database.execute(f"-- INSERT INTO passw (site, username, password) VALUES ({password.site}, {password.username}, {password.password})")
    def insert(self, password):
        self.database.execute(f"INSERT INTO passw (site, username, password) VALUES ({password.site}, {password.username}, {password.password})")
    def show(self, site):
        print(f"_{site}_")
        self.database.cursor.execute(
            f"SELECT * FROM passw WHERE site = '{site}'")
        print(self.database.cursor.fetchall())
        self.database.cursor.execute(
            f"SELECT * FROM passw")
        print(self.database.cursor.fetchall())

if __name__ == "__main__":
    pm = PM()