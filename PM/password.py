"""


Menu:
    choose
        view password
        add new password
        remove saved password
        update password option

        # create new database
"""

class password:

    def __init__(self, pm):
        pm.auth()
        self.pm = pm
        self.password:str
        self.username:str
        self.site:str
        self.date_time:str


    def menu(self):
        print("\nPlease choose the option you want to pursue.", end="\n")
        print("1. View saved password.", end="\n")
        print("2. Edit a saved password.", end="\n")
        print("3. Remove a saved password.", end="\n")

        self.choice = int(input())
        if self.choice == 1:
            site = input("Please enter the site you want to access password for: ") #make it lowercase and no spaces
            # row = self._load_from_saved(site)
            self.pm.show(site)
            # self.show() #to be created

        elif self.choice == 2:
            site = input("Please enter the site you want to access password for: ")  # make it lowercase and no spaces
            row = self._load_from_saved(site)
            new_password = input("Enter the new password: ")
            self.update(new_password)
        elif self.choice   == 3:
            site = input("Please enter the site you want to access password for: ")  # make it lowercase and no spaces
            row = self._load_from_saved(site)
            self._delete()
        else:
            print("Invalid choice\n")




    def _update(self, new_password):
        self.pm.update(self, new_password)
    def _load_from_saved(self, site:str):
        pass
        # self._load_vars(row)
    def _load_vars(self):
        pass
    def _delete(self):
        self.pm.delete(self)
    def show(self):
        pass








