import re
from datetime import datetime, date

product_list = []

class Product :
    def __init__(self, product_id , name, brand , quantity ,  price , expire_date):
        self.product_id = product_id
        self.name = name
        self.brand = brand
        self.quantity = quantity
        self.price = price
        self.expire_date = datetime.strptime(expire_date, "%Y-%m-%d").date()

    #def __ge__(self, other):
     #   return self.expire_date >= other.expire_date

    def is_valid(self):
        if not re.match(r"^[a-zA-Z\s]{3,30}$", self.name):
            raise NameError("Invalid name!")

        if not re.match(r"^[a-zA-Z\s]{3,30}$", self.brand):
            raise NameError("Invalid brand!")

        if not (type(self.quantity) == int and self.quantity > 0):
            raise NameError("Invalid quantity!")

        if not (type(self.price) == float and self.price > 0):
            raise NameError("Invalid price!")

        if not self.expire_date >= datetime.today().date():
            raise NameError("Invalid expiration date!")

        return True


    def calculate_total(product_list):
        """Calculate the total price of all products."""
        if not product_list:
            raise ValueError("No Products", "No products available.")

        total = 0
        for product in product_list:
            total += product["quantity"] * product["price"]

        return total

    def to_tuple(self):
        return tuple((self.product_id  , self.name , self.brand , self.quantity , self.price , self.expire_date ))