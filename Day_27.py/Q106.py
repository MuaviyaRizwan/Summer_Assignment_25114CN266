class Employee:
    def __init__(self, emp_id, name, dept):
        self.emp_id = emp_id
        self.name = name
        self.dept = dept

    def display(self):
        print(f"ID: {self.emp_id}, Name: {self.name}, Dept: {self.dept}")

employees = []

while True:
    print("\n1. Add Employee\n2. Display Employees\n3. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        dept = input("Enter Department: ")
        employees.append(Employee(emp_id, name, dept))
    elif choice == 2:
        for e in employees:
            e.display()
    else:
        break
