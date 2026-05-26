""" Exercise 1: 
Create a dictionary for a product: name, price, stock.
Update: the price, the stock quantity.
Print the updated dictionary. """

product = {
    "name": "Laptop",
    "price": 1200,
    "stock": 5
}

product["price"] = 1000
product["stock"] = 10

print(product)



""" Exercise 2: Create a dictionary of users. Check if the key "admin" exists. Print a message depending on the result. """

users = {
    "admin": "Alice",
    "editor": "Bob",
    "guest": "Charlie"
}

if "admin" in users:
    print("Admin exists")
else:
    print("Admin not found")



""" Exercise 3: Create a small inventory system using dictionaries.
Requirements:
  - add products
  - update stock
  - print all products  """

inventory = {
    "apple": 10,
    "banana": 5
}

# Add product
inventory["orange"] = 7

# Update stock
inventory["banana"] = 12

# Print inventory
for product, quantity in inventory.items():
    print(f"{product}: {quantity}")



""" Exercise 4: 
Create a dictionary where:
  - keys are student names
  - values are lists of grades
Requirements:
  - calculate average grade for each student
  - print students with average above 8.  """

students = {
    "Alice": [9, 8, 10],
    "Bob": [6, 7, 8],
    "Emma": [10, 9, 9]
}

for student, grades in students.items():
    average = sum(grades) / len(grades)

    if average > 8:
        print(f"{student}: {average:.2f}")



""" Exercise 5: You have a dictionary of products and sold quantities.
Requirements:
  - calculate total sold items
  - find best-selling product
  - print products with sales under 5.  """

sales = {
    "Laptop": 12,
    "Mouse": 4,
    "Keyboard": 7,
    "Monitor": 3
}

total_sales = sum(sales.values())

best_product = max(sales, key=sales.get)

print("Total sold:", total_sales)
print("Best seller:", best_product)

for product, quantity in sales.items():
    if quantity < 5:
        print("Low sales:", product)



""" Exercise 6: Create a shopping cart dictionary.
Requirements:
  - add products
  - update quantities
  - remove products
  - calculate total price.   """

cart = {
    "apple": {
        "price": 2,
        "quantity": 3
    },
    "banana": {
        "price": 1,
        "quantity": 5
    }
}

# Add product
cart["orange"] = {
    "price": 3,
    "quantity": 2
}

# Update quantity
cart["banana"]["quantity"] = 10

# Remove product
del cart["apple"]

# Calculate total
total = 0

for product, details in cart.items():
    total += details["price"] * details["quantity"]

print("Total:", total)

