class passbook:
    """
    Defines Class for the storage of transaction history.
    usage:
    keeping track of deposits, withdrawls and net balance
    """

    entry_number = 1

    def __init__(self) -> None:
        """creates the list of transactions, its type and dates"""
        self.transactions: list = []
        self.transaction_dates: list = []
        self.transaction_type: list = []

    def updatePassbook(self, deposit, withdraw):
        """
        updates the passbook for any deposits or withdrawls
        Auto assignment of dates and time can be added
        """
        if deposit:
            self.transactions.append(deposit)
            self.transaction_dates.append(passbook.entry_number)
            self.transaction_type.append("Credit")
            passbook.entry_number += 1

        if withdraw:
            self.transactions.append(withdraw)
            self.transaction_dates.append(passbook.entry_number)
            self.transaction_type.append("Debit")
            passbook.entry_number += 1

    def printPassbook(self):
        """
        prints the passbook
        includes type of transaction , amount , net balance
        """
        balance = 0
        print("S.NO  |  TYPE      |     AMOUNT   |      NET BALANCE")
        print("______|____________|______________|________________")
        for amount, type, date in \
                zip(self.transactions,
                    self.transaction_type,
                    self.transaction_dates):
            balance += amount if type == "Credit" else -amount
            print("{0:3d}   |  {1:8s}  |   {2:10.3f} |   {3:10.3f}".format(
                date, type, amount, balance))
            print("______|____________|______________|________________")
