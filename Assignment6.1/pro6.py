# Create a Bank system with SavingsAccount and CurrentAccount classes.
class SavingsAccount:
    def __init__(self, account_holder, balance=0, interest_rate=0.04):
        self.account_holder = account_holder
        self.balance = balance
        self.interest_rate = interest_rate
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. Balance: {self.balance}")
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}. Balance: {self.balance}")
        else:
            print("Insufficient balance")
    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest added {interest}. Balance: {self.balance}")
class CurrentAccount(SavingsAccount):
    def __init__(self, account_holder, balance=0, overdraft_limit=5000):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit
    def withdraw(self, amount):
        if self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
            print(f"Withdrawn {amount}. Balance: {self.balance}")
        else:
            print("Overdraft limit exceeded")
s = SavingsAccount("Meet", 10000)
s.deposit(2000)
s.withdraw(3000)
s.add_interest()
c = CurrentAccount("Alay", 5000)
c.withdraw(8000)
c.deposit(2000)

