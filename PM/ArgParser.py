# Python program to demonstrate
# command line arguments


import argparse


# msg = "outputs the sum of integers"

# Initialize parser

class CmdArgs:
    def __init__(self, pm):
        self.pm = pm
        # initializing the parser
        self.parser = argparse.ArgumentParser()

        # adding the optional arguments to the parser
        self.parser.add_argument('-i', '--insert', metavar='', nargs=3, type=str,
                                 help="format: -i <site> <username> <password>")
        self.parser.add_argument('-v', '--view', metavar='', nargs=1, type=str, help="format: -i <site>")
        self.parser.add_argument('-u', '--update', metavar='', nargs=3, type=str,
                                 help="format: -i <site> <old password> <new "
                                      "password>")
        self.parser.add_argument('-d', '--delete', metavar='', nargs=2, type=str, help="format: -i <site> <username>")
        self.parser.add_argument('-a', '--auth', metavar='', nargs=1, type=str,
                                 help="enter the master key in double quotes")

        # calling the parse args method
        self.args = self.parser.parse_args()
        self.action()

    def action(self):
        if self.args.insert:
            self.pm.current_password.insert(self.args.insert)
        if self.args.update:
            pass
        if self.args.delete:
            pass
        if self.args.view:
            pass

