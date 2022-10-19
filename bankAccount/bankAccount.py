from passbook import passbook
# from time import time


class bankAccount:
    """
    Defines a class for representation of a bank account.
    Has name, account number.
    Everything else is implemented using the passbook class.
    """
    defaulAccountNo = 1 #for assignment of the account number automatically

    def __init__(self, customer_name, deposit=0) -> None:
        """Creates the account and the passbook for the account holder"""

        #account creation and updation of defaultAccountNo
        self.accountHolderName = customer_name 
        self.accountNo = bankAccount.defaulAccountNo
        bankAccount.defaulAccountNo += 1

        #Passbook creation and updation, adding deposit to the current account balance
        self.accountBalance = deposit
        self.passbook = passbook()
        self.passbook.updatePassbook(deposit, 0)

       

    def deposit(self, amount_deposited):
        """Deposits the money in the bank account"""
        self.accountBalance += amount_deposited     #updating the current balance
        self.passbook.updatePassbook(amount_deposited, 0)      #updation of the passbook

    def withdraw(self, amount_withdrawn):
        """Debits the money from the bank account"""

        if self.accountBalance >= amount_withdrawn:
            self.accountBalance += amount_withdrawn     #current balace updation if the debit is possible
            self.passbook.updatePassbook(0, amount_withdrawn)   #passbook updataion
        else:
            print("Not Enoung Account Balance!")

    def show_transactions(self):
        """Prints the passbook for the account"""
        self.passbook.printPassbook()


if __name__ == "__main__":

    #switch case menu can be implemented instead of hardcoded transactions
    bankAccounts = bankAccount("Client 1", 10000)
    bankAccounts.deposit(5000)
    bankAccounts.withdraw(4000)
    bankAccounts.deposit(1030)
    bankAccounts.withdraw(4000)
    bankAccounts.deposit(8030)
    bankAccounts.withdraw(3000)
    bankAccounts.withdraw(1000)
    bankAccounts.deposit(8050)
    bankAccounts.deposit(5300)
    bankAccounts.withdraw(4000)
    bankAccounts.show_transactions()
