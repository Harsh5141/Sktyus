# Create a BankAccount class with deposit and withdraw methods. 
class BankAccount:
    def __init__(self,amount=33000):
        self.amount=amount
    def deposit(self,increase):
        self.amount +=increase
        print(f"Total.amount:{self.amount}RS")
    def withdraw(self,decrease):
        if decrease > self.amount:
            print("Insufficient balance!")
        else:
            self.amount -=decrease
            print(f"Total.amount:{self.amount}RS")
User=BankAccount()
User.deposit(50000)
User.withdraw(20000)