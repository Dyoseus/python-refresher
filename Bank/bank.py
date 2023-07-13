class BankAccount:
    def __init__(self, name, number, balance):
        self.name = name  
        self.number = number
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def CheckBalance(self, amount):
        return "Balance:" + str(self.balance)
