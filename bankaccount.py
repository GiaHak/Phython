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


#creating 2 users
Gia = BankAccount(0.01, 2000)
Kwasi = BankAccount(0.05, 10000)

#bankaccount display

Gia.deposit(100).deposit(300).deposit(6000).withdraw(700).yield_interest().display_account_info()

Kwasi.deposit(600).deposit(200).withdraw(250).withdraw(100).withdraw(50).withdraw(200).yield_interest().display_account_info()
