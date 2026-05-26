""" Write a Python program that:
  - defines a Student class that stores a name and a list of grades
  - defines a Catalog class that stores multiple students (has-a relationship)
Allows:
  - adding a student
  - adding grades to a student
  - computing the average grade
  - displaying all students with their averages
  - uses a menu-driven interface to interact with the system.  """


class Student:
    def __init__(self, name):
        self.name = name
        self.__grades = []

    def add_grade(self, grade):
        if 0 < grade <= 10:
            self.__grades.append(grade)

    def average(self):
        if len(self.__grades) == 0:
            return 0
        return sum(self.__grades) / len(self.__grades)


class Catalog:
    def __init__(self):
        self.__students = []

    def add_student(self, student):
        self.__students.append(student)

    def find_student(self, name):
        for student in self.__students:
            if student.name == name:
                return student
        return None

    def show_all(self):
        for student in self.__students:
            print(f"Name: {student.name}, Average: {student.average()}")


def main():
    catalog = Catalog()

    while True:
        try:
            print("\n--- CATALOG MENU ---")
            print("1. Add student")
            print("2. Add grade to student")
            print("3. Show all students")
            print("4. Exit")

            option = input("Choose an option: ")

            if option == "1":
                name = input("Enter student name: ")
                student = Student(name)
                catalog.add_student(student)
                print("Student added successfully!")

            elif option == "2":
                name = input("Enter student name: ")
                student = catalog.find_student(name)

                if student:
                    grade = float(input("Enter grade: "))
                    student.add_grade(grade)
                else:
                    print("Student not found!")

            elif option == "3":
                catalog.show_all()

            elif option == "4":
                print("Goodbye!")
                break

            else:
                print("Invalid option!")

        except ValueError:
            print("Error: invalid input type!")
        except Exception as e:
            print("Unexpected error:", e)


if __name__ == "__main__":
    main()
