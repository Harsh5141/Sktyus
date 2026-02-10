# 2. Bank Management System
class Bankaccount:
    def __init__(self, acc_no, name, balance=0):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposite successfully.")
        else:
            print("invalid deposite amount.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdraw successfully.")
        else:
            print("insufficient balance.")

    def check_balance(self):
        print("Current_balance:", self.balance)

    def display_detail(self):
        print("Account_no:", self.acc_no)
        print("Account_holder:", self.name)
        print("Balance:", self.balance)


account = None
while True:
    print("\n----Bank Management System----")
    print("1.Create Account")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Check Balabce")
    print("5.Display Account Details")
    print("6.Exit")
    choice = input("Enter your choice:")
    if choice == "1":
        acc_no = input("Enter Account Number:")
        name = input("Enter Account Holder Name:")
        account = Bankaccount(acc_no, name)
        print("Account Created Successfully.")
    elif choice == "2":
        if account:
            amount = float(input("Enter your Amount:"))
            account.deposit(amount)
        else:
            print("create an account first.")
    elif choice == "3":
        if account:
            amount = float(input("Enter your Amount:"))
            account.withdraw(amount)
        else:
            print("create an account first.")
    elif choice == "4":
        if account:
            account.check_balance()
        else:
            print("create an account first.")
    elif choice == "5":
        if account:
            account.display_detail()
        else:
            print("create an account first.")
    elif choice == "6":
        if account:
            print("Thank you for using this system.")
            break
        else:
            print("Invalid choice.Try again.")

# 5. Simple E-commerce cart system
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class Cart:
    def __init__(self):
        self.items = []
    def add_product(self, product):
        self.items.append(product)
        print(f"{product.name} added to cart.")
    def remove_product(self, product_name):
        for item in self.items:
            if item.name == product_name:
                self.items.remove(item)
                print(f"{product_name} removed from cart.")
                return
        print("Product not found in cart.")
    def view_cart(self):
        if not self.items:
            print("Cart is empty.")
            return
        print("\nItems in Cart:")
        for item in self.items:
            print(f"- {item.name} : ₹{item.price}")
    def total_amount(self):
        total = sum(item.price for item in self.items)
        print("Total Amount: ₹", total)
cart = Cart()
while True:
    print("\n--- Simple E-Commerce Cart ---")
    print("1. Add Product")
    print("2. Remove Product")
    print("3. View Cart")
    print("4. Total Amount")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        p = Product(name, price)
        cart.add_product(p)
    elif choice == "2":
        name = input("Enter product name to remove: ")
        cart.remove_product(name)
    elif choice == "3":
        cart.view_cart()
    elif choice == "4":
        cart.total_amount()
    elif choice == "5":
        print("Thank you for shopping!")
        break
    else:
        print("Invalid choice. Try again.")