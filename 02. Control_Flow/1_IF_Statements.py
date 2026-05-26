""" Exercise 1: A streaming platform grants access based on subscription type and user conditions.
  Write a Python program that reads the user’s age, subscription type (1 = Standard, 2 = Premium, 3 = No subscription)
  and number of days of payment delay, then prints one result:
    - “Access blocked” if the user is under 16 or has more than 30 days of delay
    - “Full access” if the user has a Premium subscription and 0 days of delay
    - “Limited access” in all other cases """

age = int(input("Enter age: "))
subscription = int(input("Enter subscription type (1 = Standard, 2 = Premium, 3 = No subscription): "))
delay = int(input("Enter number of delay days: "))

if age < 16 or delay > 30:
    print("Access blocked")
elif subscription == 2 and delay <= 5:
    print("Full access")
elif (subscription == 1 and delay <= 10) or (subscription == 3 and delay == 0):
    print("Limited access")
else:
    print("Invalid input data")



""" Exercise 2: A message validation system checks whether a text can be publicly displayed.

Write a Python program that reads the user’s age, a message, and whether the message is marked as official (1 = yes, 0 = no), 
then processes and analyzes the message:
  - Convert the message to uppercase and lowercase
  - Replace all occurrences of “secret” with “*****”
  - Compute: message length, number of “*****” occurrences, first character, last character, and reversed message
Then print one result:
  - “Message rejected” if the user is under 18, or the message has fewer than 12 characters, or it starts with a digit
  - “Message valid” if the user is at least 18, the message is marked as official, “secret” appears at most once, and it does not end with “!”
  - “Message for review” in all other cases """

age = int(input("Enter age: "))
message = input("Enter message: ")
official = int(input("Is the message official? (1 = yes, 0 = no): "))

message = message.upper()
message = message.lower()
message = message.replace("secret", "*****")

length = len(message)
occurrences = message.count("*****")
first_char = message[0]
last_char = message[-1]
reversed_message = message[::-1]

if age < 18 or length < 12 or first_char.isdigit():
    print("Message rejected")

elif age >= 18 and official == 1 and occurrences <= 1 and last_char != "!":
    print("Message valid")

else:
    print("Message for review")



""" Exercise 3: An automated system analyzes two messages sent by a user and decides the account action.
Write a Python program that reads the user’s age, two messages, and account type (1 = normal, 2 = verified), then processes each message:
For each message:
  - convert to lowercase
  - replace all occurrences of “spam” with “###”
  - convert to uppercase
  - create a reversed version
Then analyze:
  - length of each message
  - total occurrences of “###” in both messages
  - first character of the first message
  - last character of the second message
  - first character of each reversed message
Finally, print one result:
  - “Account suspended” if the user is under 18, or any message has fewer than 25 characters, or the first message starts with a digit, 
    or the second message ends with a digit
  - “Account approved” if the user is at least 18, the account is verified, “###” appears at most twice in total,
    neither message ends with “!”, and the first character of each reversed message is not a digit
  - “Account under review” in all other cases  """

age = int(input("Enter age: "))
first_message = input("Enter first message: ")
second_message = input("Enter second message: ")
account_type = int(input("Account type (1 = normal, 2 = verified): "))

first_message = first_message.lower()
second_message = second_message.lower()

first_message = first_message.replace("spam", "###")
second_message = second_message.replace("spam", "###")

first_message = first_message.upper()
second_message = second_message.upper()

reversed_1 = first_message[::-1]
reversed_2 = second_message[::-1]

length_1 = len(first_message)
length_2 = len(second_message)

occurrences_1 = first_message.count("###")
occurrences_2 = second_message.count("###")

first_char = first_message[0]
last_1 = first_message[-1]
last_2 = second_message[-1]

first_rev_1 = reversed_1[0]
first_rev_2 = reversed_2[0]

if age < 18 or (length_1 < 25 or length_2 < 25) or first_char.isdigit() or last_2.isdigit():
    print("Account suspended")

elif age >= 18 and account_type == 2 and (occurrences_1 + occurrences_2 <= 2) and last_1 != "!" and last_2 != "!" and not first_rev_1.isdigit() and not first_rev_2.isdigit():
    print("Account approved")

else:
    print("Account under review")
