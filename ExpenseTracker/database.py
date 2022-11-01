import sqlite3 as sql


class Database:
    def __init__(self):
        # connecting to the database and creating the cursor object
        self.database = sql.connect("expense.db")
        self.cursor = self.database.cursor()

        table_columns = {"category": "VARCHAR(255)", "amount": "float8",
                         "date": "datetime DEFAULT(DATE('now'))"}

        table_check = self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='table_name'")
        # print(table_check)
        if not table_check:
            self._create_table("expenses", table_columns)
        print(table_check.fetchall())

    def _create_table(self, name, columns: dict = None):
        create_command = f"CREATE TABLE IF NOT EXISTS {name} (ID INTEGER PRIMARY KEY AUTOINCREMENT)"
        self.execute(create_command, commit=True)

        for col, type in columns.items():
            self.execute(f"ALTER TABLE {name} ADD COLUMN {col} {type}", commit=True)

    def execute(self, command, commit=0):
        print(f"command executed: {command}")  # Debugging
        self.cursor.execute(command)

        # commits if the operation required it
        if commit:
            self.database.commit()



if __name__ == "__main__":
    database = Database()
