""" 
Write a Python program that:
  - reads data from a file called students.csv
  - each line contains a student name and their house, separated by a comma
  - stores the data in a list of dictionaries
  - sorts the students alphabetically by name
  - prints each student in the format: "Name is in House".  """

students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")



""" Exercise 2:
Write a Python program that:
  - asks the user for a name, home, and age
  - appends this data to a CSV file called students.csv
  - uses csv.DictWriter
  - writes the fields: name, home, age into the file.   """

import csv

name = input("Name: ").strip()
home = input("Home: ").strip()
age = int(input("Age: ").strip())

with open("students.csv", "a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home", "age"])
    writer.writerow({
        "name": name,
        "home": home,
        "age": age
    })
  
