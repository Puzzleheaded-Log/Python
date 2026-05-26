"""
Write a Python program that:
  - manages a student registry stored in a CSV file
  - allows adding a student (name, house, age)
  - prevents duplicate entries (with confirmation)
  - displays all students
  - searches for a student by name
  - uses csv.DictReader and csv.DictWriter
  - handles file errors and invalid input gracefully.  """

import csv
import os


def add_student():
    name = input("Name: ").strip()
    house = input("House: ").strip()
    age = int(input("Age: "))

    if os.path.exists("students.csv"):
        with open("students.csv") as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row["Name"].lower() == name.lower():
                    answer = input("Student already exists. Add anyway? (yes/no): ")
                    if answer.lower() == "no":
                        print("Operation cancelled!")
                        return
                    break

    with open("students.csv", "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "House", "Age"])

        if file.tell() == 0:
            writer.writeheader()

        writer.writerow({
            "Name": name,
            "House": house,
            "Age": age
        })

    print("Student added successfully!")


def view_students():
    try:
        with open("students.csv") as file:
            reader = csv.DictReader(file)
            students = list(reader)

            if not students:
                print("No students found!")
                return

            for row in students:
                print(f"{row['Name']} | {row['House']} | {row['Age']}")

    except FileNotFoundError:
        print("No student file found!")


def search_student():
    name = input("Name: ").lower()
    found = False

    try:
        with open("students.csv") as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row["Name"].lower() == name:
                    print(f"Student found: {row['Name']} | {row['House']} | {row['Age']}")
                    found = True
                    break

            if not found:
                print("Student not found!")

    except FileNotFoundError:
        print("No student file found!")


while True:
    try:
        print("\nStudent Registry")
        print("1. Add student")
        print("2. View all students")
        print("3. Search student")
        print("4. Exit")

        option = int(input("\nChoose option: "))

        if option == 1:
            add_student()

        elif option == 2:
            view_students()

        elif option == 3:
            search_student()

        elif option == 4:
            print("Goodbye!")
            break

    except ValueError:
        print("Invalid input!")

    except Exception as e:
        print(f"Error: {e}")


