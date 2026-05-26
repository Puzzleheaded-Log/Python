""" Exercise 1: Write a program with a predefined password (e.g. "python") that asks the user to enter the password using a while loop. 
The user has a maximum of 3 attempts. Print:
  - “Login successful” if the password is correct
  - “Wrong password” if the password is incorrect
  - “Access blocked” after 3 failed attempts  """

password = "Python"
attempts = 0
user_password = ""

while user_password != password and attempts < 3:
    user_password = input("Enter password: ")
    attempts += 1

    if user_password != password:
        print("Wrong password")

if user_password == password:
    print("Login successful")
else:
    print("Access blocked")



""" Exercise 2: Write a program that simulates a simple banking system.
Requirements:
  - Initial balance is 1000 RON
  - The user can withdraw an amount (integer input)
  - Maximum of 4 attempts are allowed
  - If the user enters 0, the program stops immediately
Rules:
  - If withdrawal amount is greater than the balance → print “Insufficient funds”
  - If withdrawal amount is valid → subtract it from the balance and display the remaining balance  """

initial_balance = 1000
attempts = 0
withdraw_amount = -1

while withdraw_amount != 0 and attempts < 4:
    withdraw_amount = int(input("Enter withdrawal amount (0 to exit): "))
    attempts += 1

    if withdraw_amount == 0:
        print("No withdrawal made")
        break

    if withdraw_amount > initial_balance:
        print("Insufficient funds")
    else:
        initial_balance = initial_balance - withdraw_amount
        print("Remaining balance:", initial_balance)



""" Exercise 3: Write a program that simulates fuel refueling at a gas station.
Requirements:
  - Initial fuel tank is 50 liters
  - The user can make a maximum of 4 attempts
  - At each attempt, the user enters the number of liters they want
Rules:
  - If the user enters 0 → print “Refueling cancelled” and stop
  - If requested liters exceed available fuel → print “Insufficient fuel”
  - If valid → subtract from tank and print remaining fuel
  - If fuel reaches 0 → stop the program   """

tank = 50
attempts = 0
liters = -1

while liters != 0 and tank != 0 and attempts < 4:
    liters = int(input("Enter fuel amount (0 to cancel): "))
    attempts += 1

    if liters == 0:
        print("Refueling cancelled")
        break

    if liters > tank:
        print("Insufficient fuel")
    else:
        tank = tank - liters
        print("Remaining fuel in tank:", tank, "liters")



""" Exercise 4: Create a program that manages a product list.
Initial list: products = ["kiwi", "plant milk", "oats", "onion"]
The user can enter:
  - "add" → add a product
  - "del" → delete a product
  - "show" → display the list
  - "exit" → stop the program
The program should not crash if the product does not exist.  """

products = ["kiwi", "plant milk", "oats", "onion"]

text = ""

while text != "exit":
    text = input("""
For adding a product type add
For deleting a product type del
For showing the list type show
To exit type exit
: """).lower()

    if text == "exit":
        print("You exited the program")
        break

    elif text == "add":
        product = input("Enter a product: ")

        while product in products:
            print("Product already exists!")
            product = input("Enter another product: ")

        products.append(product)

    elif text == "del":
        product_to_delete = input("Enter a product to delete: ")

        while product_to_delete not in products:
            print("Product not found in list!")
            product_to_delete = input("Enter a valid product: ")

        products.remove(product_to_delete)

    elif text == "show":
        print(products)

    else:
        print("Invalid command!")
      

