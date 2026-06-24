class Employee:
    def __init__(self, emp_id, name, dept):
        self.emp_id = emp_id
        self.name = name
        self.dept = dept

    def display(self):
        print(f"ID: {self.emp_id}, Name: {self.name}, Dept: {self.dept}")

employees = {}

while True:
    print("\n1. Add Employee\n2. Display All\n3. Search by ID\n4. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        dept = input("Enter Department: ")
        employees[emp_id] = Employee(emp_id, name, dept)
    elif choice == 2:
        for e in employees.values():
            e.display()
    elif choice == 3:
        emp_id = input("Enter Employee ID: ")
        if emp_id in employees:
            employees[emp_id].display()
        else:
            print("Not Found")
    elif choice == 4:
        break
