class User:

    def __init__(self, name):
        self.name = name
        self.amount = 1000

    def make_deposit(self, amount):
        self.amount += amount

    def make_withdrawl(self,amount):
        self.amount -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")
        
#Create 3 instances of the User class

Gia = User("Gia")
Kwasi = User("Kwasi")
Nick = User("Nick")

#1st user make 3 deposits and 1 withdrawal

Gia.make_deposit(20000)
Gia.make_deposit(4000)
Gia.make_deposit(700)
Gia.make_withdrawl(10000)
Gia.display_user_balance()

#2nd user make 2 deposit and  make 2 withdrawal

Kwasi.make_deposit(8000)
Kwasi.make_deposit(3500)
Kwasi.make_withdrawl(1400)
Kwasi.make_withdrawl(800)
Kwasi.display_user_balance()

#3rd user make 1 deposit  and 3 withdrawals

Nick.make_deposit(16000)
Nick.make_withdrawl(3500)
Nick.make_withdrawl(8000)
Nick.make_withdrawl(300)
Nick.display_user_balance()
