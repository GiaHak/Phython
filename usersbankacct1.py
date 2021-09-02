class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.balance = balance
        self.int_rate = int_rate

    def deposit(self, amount):
        self.balance = amount + self.balance
        return self

    def withdraw(self, amount):
        if self.balance >= amount: 
            self.balance = self.balance - amount
        else: 
            print("Insufficient funds: Charging a $5 fee")
            self.balance = self.balance - 5
        return self

    def display_account_info(self):
        print("Balance:", self.balance)
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * self.int_rate
        else: 
            print("balance is negative")
        return self

class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        
    def make_deposit(self, amount):
        self.balance.deposit(amount)
       # print(self.balance) // Show the balance
        return self
    def make_withdraw(self, amount):
        self.balance.withdraw(amount)
        return self

    def display_user_balance(self):
        self.balance.display_account_info()
        return self

Gia = User("Gia", BankAccount(0.01, 100))
# print(Gia.bankaccount.balance)
Gia.make_deposit(500)
Gia.make_withdraw(200)
Gia.display_user_balance()

