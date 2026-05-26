""" Write a Python program that implements a Company Employee Management System using OOP.
The program should:
  - Define an Employee class with name and base salary
  - Define a Manager class that inherits from Employee and adds a bonus
  - Define a Company class that stores multiple employees (has-a relationship)
Allow:
  - adding employees and managers
  - removing employees
  - calculating individual salaries (with polymorphism)
  - calculating total salaries
  - displaying all employees
Use a menu-based interface
Handle invalid input using try/except.   """

class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.salary = base_salary

    def calculate_salary(self):
        return self.salary

    def __str__(self):
        return f"Name: {self.name} | Salary: {self.salary} lei"


class Manager(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        total_salary = self.salary + self.bonus
        return total_salary

    def __str__(self):
        return f"Manager Name: {self.name} | Total Salary: {self.calculate_salary()} lei"


class Company:
    def __init__(self):
        self.__employees = []

    def find_employee(self, name):
        for employee in self.__employees:
            if employee.name == name:
                return employee
        return None

    def add_employee(self, employee):
        if self.find_employee(employee.name):
            print("Employee already exists in the company")
        else:
            self.__employees.append(employee)
            print("Employee added successfully!")

    def remove_employee(self, employee):
        if employee is None:
            print("Employee does not exist!")
        else:
            self.__employees.remove(employee)
            print("Employee removed successfully!")

    def calculate_total_salaries(self):
        total = 0
        for employee in self.__employees:
            total += employee.calculate_salary()
        return total

    def show_employees(self):
        if not self.__employees:
            print("No employees found!")
            return

        print("\nEmployees list:")
        for employee in self.__employees:
            print(employee)


def main():
    company = Company()

    while True:
        try:
            print("\nCOMPANY MANAGEMENT MENU:")
            print("\n1. Add employee")
            print("2. Add manager")
            print("3. Remove employee")
            print("4. Show employees")
            print("5. Show total salaries")
            print("6. Exit")

            option = int(input("\nChoose an option: "))

            if option == 1:
                name = input("Employee name: ")
                salary = int(input("Employee salary: "))
                employee = Employee(name, salary)
                company.add_employee(employee)

            if option == 2:
                name = input("Manager name: ")
                salary = int(input("Manager salary: "))
                bonus = int(input("Manager bonus: "))
                manager = Manager(name, salary, bonus)
                company.add_employee(manager)

            if option == 3:
                name = input("Employee name: ")
                employee = company.find_employee(name)
                company.remove_employee(employee)

            if option == 4:
                company.show_employees()

            if option == 5:
                print(f"Total salaries: {company.calculate_total_salaries()}")

            if option == 6:
                print("Exit")
                break

        except ValueError:
            print("Invalid input!")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
    
