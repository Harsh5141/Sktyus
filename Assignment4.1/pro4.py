#4 ATM withdrawal check: sufficient balance or not.
balance=33000
amount=int(input("Enter a amount: "))
if balance >= amount:
    print("sufficient balance")
else:
     print("sufficient not balance")