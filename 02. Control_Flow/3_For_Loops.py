""" Exercise 1: Write a program that prints all numbers between 1 and 100 that are divisible by 3. """

for x in range(1,101):
    if x%3==0:
        print(x)


""" Exercise 2: Write a program that reads 5 passwords and stores only the valid ones in a list.
A password is valid if:
  - it has at least 6 characters
  - it does not contain spaces
At the end, print the list of valid passwords.  """

valid_passwords = []

for x in range(5):
    password = input("Password: ")

    if len(password) >= 6 and " " not in password:
        valid_passwords.append(password)
    else:
        print("Invalid password")

print(valid_passwords)





