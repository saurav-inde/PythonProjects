import sys

from database import Database
from cmdargs import CmdArgs
from aes import AESCipher
import clipboard
from sys import argv, exit


class PM:
    def __init__(self):
        self.cipher = None
        # print(argv, end='\n')
        self.argparser = CmdArgs(self)
        self.arg = self.argparser.args
        # print("Action not yet called")

        self.database = Database()

        self.auth()
        # print("action have been called")
        self.argparser.action()

    def auth(self):
        if len(self.argparser.set_args) + len(argv) == \
                len(set(argv).union(self.argparser.set_args)):
            print(f"No arguments from {self.argparser.set_args} entered")
            print("Use 'pm -h' for help")
            exit()

        key = input("Enter the master key: ")
        self.cipher = AESCipher(key)

    def delete(self):
        command = "DELETE FROM passw WHERE site='{0}' AND username = '{1}'".format(self.arg.delete[0],
                                                                                   self.arg.delete[1])
        self.database.execute(command, commit=1)

    def update(self):
        new_password = self.cipher.encrypt(self.arg.update[2])
        command = f"UPDATE passw SET password = \"{new_password}\" WHERE site =" \
                  f" '{self.arg.update[0]}' AND username ='{self.arg.update[1]}'"
        self.database.execute(
            command, commit=1)

    def insert(self):
        password = self.cipher.encrypt(self.arg.insert[2])
        command = "INSERT INTO passw (site, username, password) VALUES" +\
                  f"('{self.arg.insert[0]}', '{self.arg.insert[1]}', \"{password}\")"
        # print(command)
        self.database.execute(command, 1)

    def show(self):
        if self.arg.view[0] != "*":
            print(f"Passwords for {self.arg.view[0]}:\n")
            command = f"SELECT * FROM passw WHERE site = '{self.arg.view[0]}'"
        else:
            command = f"SELECT * FROM passw"

        self.database.cursor.execute(command)

        fetched = self.database.cursor.fetchall()
        if not fetched:
            print("No Entries were found.")
            return

        print(" " + "_" * 95)
        print("|{0:3}|{1:^30}|{2:^30}|{3:^30}|".format("#", "Application", "Username", "Password"))
        print("|" + "_" * 95 + "|")

        for i, fetch in zip(range(len(fetched)), fetched):
            print("|{0:^3}|{1:^30}|{2:^30}|{3:^30}|".format(i + 1, fetch[0], fetch[1], "**********"))
            # print("|{0:^30}|{1:^30}|{2:^30}|".format(fetch[0], fetch[1], fetch[2]))

            print(" " + "_" * 95)
        sno = int(input("Enter S.NO of password you want to access: "))

        if sno > len(fetched):
            print("Please Enter valid S.NO")
            return

        clipboard.copy(self.cipher.decrypt(fetched[sno - 1][2]))
        print(f"!! Password for {fetched[sno - 1][0]} {fetched[sno - 1][1]} copied to the clipboard.")


if __name__ == "__main__":
    pm = PM()
