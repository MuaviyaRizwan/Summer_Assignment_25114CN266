class Salary:
    def __init__(self, emp_id, name, basic):
        self.emp_id = emp_id
        self.name = name
        self.basic = basic
        self.hra = 0.2 * basic
        self.da = 0.1 * basic
        self.total = basic + self.hra + self.da

    def display(self):
        print(f"ID: {self.emp_id}, Name: {self.name}, Total Salary: {self.total}")

salaries = []

while True:
    print("\n1. Add Salary Record\n2. Display Salaries\n3. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        basic = float(input("Enter Basic Salary: "))
        salaries.append(Salary(emp_id, name, basic))
    elif choice == 2:
        for s in salaries:
            s.display()
    else:
        break
