# Create a Laptop class with a method to apply discounts on price. 
class Leptop:
    def __init__(self,company_name,modal,price):
        self.company_name=company_name
        self.modal=modal
        self.price=price
    def discounts(self):
        discount = (self.price/100)*10
        discount_amount=self.price-discount
        print(discount_amount)
price=Leptop("HP","Victus",75000)
price.discounts()