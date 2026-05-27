""" Manage a shopping list.
Features:
  - add items
  - remove items
  - show list
  - exit.    """


shopping = []

command = ""

while command != "exit":
    command = input("add/remove/show/exit: ").lower()

    if command == "add":
        item = input("Item: ")
        shopping.append(item)

    elif command == "remove":
        item = input("Item: ")

        if item in shopping:
            shopping.remove(item)

    elif command == "show":
        print(shopping)

print("Program ended")

