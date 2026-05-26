""" Exercise 1: 
Write a Python program that:
  - asks the user for a phone number
  - validates Romanian phone number formats using a regular expression
  - accepts formats like continuous digits or separated with spaces/dashes
  - prints whether the phone number is valid or invalid.  """

import re

phone_number = input("What is your phone number? ").strip()

pattern = r"^(07[0-9]{8}|07[0-9]{2}-[0-9]{3}-[0-9]{3}|07[0-9]{2} [0-9]{3} [0-9]{3})$"

if re.search(pattern, phone_number):
    print("Valid phone number")
else:
    print("Invalid phone number")



""" Exercise 2:
Write a Python program that:
  - asks the user for a password
  - validates it using a regular expression
  - ensures it has at least 8 characters
  - contains at least 1 uppercase letter
  - contains at least 1 digit
  - prints whether the password is valid or invalid.   """

import re

password = input("Password: ")

pattern = r"^(?=.*[A-Z])(?=.*\d).{8,}$"

if re.search(pattern, password):
    print("Valid password")
else:
    print("Invalid password")


