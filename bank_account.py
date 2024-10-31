class AccountDB:
    def __init__(self):
        self.account_database = []

    def __str__(self):
        return f"The current database: {self.account_database}"

    def insert(self, item):
        self.account_database.append(item)

    def search(self, item):
        for i in range(len(self.account_database)):
            if self.account_database[i]["account_number"] == item:
                return i
        return -1

    def delete(self, item):
        self.account_database.remove(item)