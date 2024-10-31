class Account:
    def __init__(self, account_number, type, account_name, balance):
        self.account_number = account_number
        self.type = type
        self.account_name = account_name
        self.balance = balance
        self.base = AccountDB()

    def create_account(self):
        index = self.base.search(self.account_number)
        if index == -1:
            account = {}
            account["account_number"] = self.account_number
            account["type"] = self.type
            account["account_name"] = self.account_name
            account["balance"] = self.balance
            self.base.insert(account)
            if self.base.account_database != []:
                print("Insertion Complete")
        else:
            print("Account", self.account_number, "already exists")

    def delete_account(self):
        index = self.base.search(self.account_number)
        if index != -1:
            print("Deleting account:", self.base.account_database[index]["account_number"])
            del self.base.account_database[index]
        else:
            print(self.account_number, "invalid account number; nothing to be deleted.")

    def deposit(self, amount):
        index = self.base.search(self.account_number)
        if index != -1:
            print("Depositing", amount, "to", self.base.account_database[index]["account_number"])
            self.base.account_database[index]["balance"] += amount
        else:
            print(self.account_number, "invalid account number; no deposit action performed.")

    def withdraw(self, amount):
        index = self.base.search(self.account_number)
        if index != -1:
            if self.base.account_database[index]["balance"] >= amount:
                print("Withdrawing", amount, "from", self.base.account_database[index]["account_number"])
                self.base.account_database[index]["balance"] -= amount
            else:
                print("withdrawal amount", amount, "exceeds the balance of", self.base.account_database[index]["balance"], "for", self.account_number, "account.")
        else:
            print(self.account_number, "invalid account number; no withdrawal action performed.")

    def show_account(self, number):
        index = self.base.search(number)
        if index != -1:
            print("Showing details for", self.base.account_database[index]["account_number"])
            print(self.base.account_database[index])
        else:
            print(self.account_number, "invalid account number; nothing to be shown for.")

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