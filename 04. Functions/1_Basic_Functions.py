""" Exercise 1: Input Validation
Write a function called read_positive_number that:
  - asks the user for a number
  - uses a while loop until the number is greater than 0
  - returns the number.   """

def read_positive_number():
    number = int(input("Number: "))

    while number <= 0:
        print("Please enter a positive number!")
        number = int(input("Number: "))

        if number > 0:
            break

    return number

print(read_positive_number())



""" Exercise 2: Divisors
Write a function called divisors that:
  - receives a number
  - displays all of its divisors.  """

def divisors(number):
    divisors_list = []

    for x in range(1, number):
        if number % x == 0:
            divisors_list.append(x)

    return divisors_list

print(divisors(10))



""" Exercise 3: Sum Until Stop
Write a function called sum_until_stop() that:
  - reads numbers from the keyboard
  - stops when the user enters 0
  - returns the sum of the entered numbers.  """

def sum_until_stop():
    numbers = []

    while True:
        number = input("Number: ")

        if not number.isdigit():
            print("Invalid input!")
            continue

        converted_number = int(number)

        if converted_number == 0:
            break

        numbers.append(converted_number)

    return sum(numbers)

print(sum_until_stop())



""" Exercise 4: 
Write a function called max_student() that:
  - receives a dictionary containing student names and grades
  - finds the student with the highest grade
  - displays the student's name and grade.   """

grades = {
    "Ana": 9,
    "Ion": 7,
    "Maria": 10
}

def max_student(grades_dictionary):
    highest_grade = 0
    student = ""

    for name, grade in grades_dictionary.items():
        if grade > highest_grade:
            highest_grade = grade
            student = name

    print(f"{student}: {highest_grade}")

max_student(grades)
