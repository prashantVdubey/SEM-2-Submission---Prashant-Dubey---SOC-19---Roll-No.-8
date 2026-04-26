# Experiment 7: Multiple Inheritance

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print(f'Name : {self.name}')
        print(f'Age  : {self.age}')

    def greet(self):
        print(f'Hello! I am {self.name}.')


class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def display_employee(self):
        self.display_person()
        print(f'Emp ID : {self.employee_id}')
        print(f'Salary : Rs. {self.salary:,.2f}')

    def show_salary(self):
        print(f'{self.name} earns Rs. {self.salary:,.2f} per month.')


class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department, team_size):
        super().__init__(name, age, employee_id, salary)
        self.department = department
        self.team_size = team_size

    def display_manager(self):
        self.display_employee()
        print(f'Dept  : {self.department}')
        print(f'Team  : {self.team_size} members')

    def conduct_meeting(self):
        print(f'{self.name} is conducting a team meeting for {self.department}.')

    def approve_leave(self, emp_name):
        print(f'{self.name} approved leave for {emp_name}.')


# Main Program
print('=== Person ===',)
p = Person('Aarav', 25)
p.display_person()
p.greet()

print('\n=== Employee ===')
e = Employee('Priya', 30, 'E1023', 55000)
e.display_employee()
e.show_salary()

print('\n=== Manager ===')
m = Manager('Suresh', 42, 'M501', 120000, 'Engineering', 12)
m.display_manager()
m.conduct_meeting()
m.approve_leave('Priya')
m.greet()  # Inherited from Person
