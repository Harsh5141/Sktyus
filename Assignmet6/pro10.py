# Create a Shop class with a method to add and list products.
class Shop:
    def __init__(self, name):
        self.name = name
        self.products = [] 

    def add_product(self, product_name, product_price):
        product = {"name": product_name, "price": product_price}
        self.products.append(product)
        print(f"Product '{product_name}' added successfully!")

    def list_products(self):
        if not self.products:
            print("No products in the shop.")
        else:
            print(f"Products in {self.name}:")
            for idx, product in enumerate(self.products, start=1):
                print(f"{idx}. {product['name']} - ${product['price']}")

my_shop = Shop("HP")
my_shop.add_product("Laptop", 800)
my_shop.add_product("Mouse", 25)
my_shop.list_products()
