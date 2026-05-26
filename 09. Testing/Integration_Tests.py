"""Write unit tests for a Product class that:
  - creates a test product
  - tests stock addition
  - tests product selling
  - tests discount application
  - verifies the final price
  - verifies the final stock
  - verifies the total stock value using assert. """

class Product:

    def __init__(self, product_name, price, stock=0):
        # self represents the current object reference

        if price < 0:
            raise ValueError("Invalid price")

        if stock < 0:
            raise ValueError("Invalid stock")

        # Instance attributes
        self.name = product_name
        self.price = price
        self.stock = stock

    def add_stock(self, quantity):
        if quantity <= 0:
            raise ValueError("Invalid quantity")

        self.stock = self.stock + quantity

    def sell_product(self, quantity):
        if quantity <= 0:
            raise ValueError("Invalid quantity")

        if quantity > self.stock:
            raise ValueError("Quantity is greater than stock")

        self.stock = self.stock - quantity

    def apply_discount(self, percent):
        if percent < 0 or percent > 100:
            raise ValueError("Invalid percentage")

        discount = percent / 100 * self.price
        self.price = self.price - discount

    def total_stock_value(self):
        return self.price * self.stock



#Testing the function
from tested_file import Product

def test_complete_operations_flow():

    # Create a test product
    product = Product("banana", 2.0, 18)

    # Add stock
    product.add_stock(2)

    # Sell products
    product.sell_product(5)

    # Apply discount
    product.apply_discount(20)

    # Verify final values
    assert product.price == 1.6
    assert product.stock == 15
    assert product.total_stock_value() == 24.0

