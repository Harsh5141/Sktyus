# Create a Book class to store title, author, and price, and display details. 
class Book:
    def __init__(self,title,author,price):
        self.title=title 
        self.author=author
        self.price=price
    def display(self):
        print("Book_Title:",self.title)
        print("Author_Name:",self.author)
        print("Book_Price:",self.price,"RS")
book1=Book("Python Programming","Gudio","850")
book1.display()