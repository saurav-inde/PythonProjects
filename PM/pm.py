import sys
from password import password
from database import database
from hash import sha_512
from ArgParser import CmdArgs


class PM:
    def __init__(self):

        self.user_default = {"host": "localhost",
                             "password": "2050",
                             "username": "root",
                             "database": "pm"
                             }
        self.user = self.user_default

        self.authenticated = False
        self.current_password = password(self)
        self.database = database(self)
        self.argparser = CmdArgs(self)
        self.auth()
        if not self.authenticated:
            print("Sorry, your identity could not be authenticated!")
            sys.exit()

        while self.current_password.choice:
            self.current_password.menu()
            self.current_password = password(self)

    def auth(self):

        try:
            with open(".backup", "r") as bakp:
                hash_value = bakp.read()
                if hash_value:
                    key = ""
                    if self.argparser.args.auth:
                        key = self.argparser.args.auth
                    else:
                        key = input("Enter the masterkey for authentication: ")
                    print(sha_512(key), end="\n")
                    print(hash_value)
                    if sha_512(key) == hash_value:
                        self.authenticated = True
                        return
                    else:
                        print("Authentication failure!")
        except:
            print("No Database found...\n")
            print("CREATING DATABASE\n")

            with open(".backup", "w") as bakp:
                master_key = input("Choose a masterkey for your passwords: ")
                bakp.write(sha_512(master_key))
        # self.auth()

    def delete(self, password):
        self.database.execute("DELETE FROM passw WHERE site='{0}'".format(password.site), 1)

    def update(self, password):
        command = f"UPDATE passw SET password = '{password.password}' WHERE site = '{password.site}'"
        self.database.execute(
            command, commit=1)

    def insert(self, password):
        command = "INSERT INTO passw (site, username, password) VALUES" + f"('{password.site}', '{password.username}', '{password.password}')"
        print(command)
        self.database.execute(command, 1)

    def show(self, site):
        print(f"_{site}_")
        self.database.cursor.execute(
            f"SELECT * FROM passw WHERE site = '{site}'")
        print(self.database.cursor.fetchall())
        # print(self.database.cursor.fetchall())


if __name__ == "__main__":
    pm = PM()
