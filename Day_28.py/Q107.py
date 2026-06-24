class Salary:
    def __init__(self, emp_id, name, basic, hra, da):
        self.emp_id = emp_id
        self.name = name
        self.basic = basic
        self.hra = hra
        self.da = da

    def total_salary(self):
        return self.basic + self.hra + self.da

    def display(self):
        print(f"ID: {self.emp_id}, Name: {self.name}, Total Salary: {self.total_salary()}")

salaries = {}

while True:
    print("\n1. Add Salary Record\n2. Display All\n3. Search by ID\n4. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        basic = float(input("Enter Basic Salary: "))
        hra = float(input("Enter HRA: "))
        da = float(input("Enter DA: "))
        salaries[emp_id] = Salary(emp_id, name, basic, hra, da)
    elif choice == 2:
        for s in salaries.values():
            s.display()
    elif choice == 3:
        emp_id = input("Enter Employee ID: ")
        if emp_id in salaries:
            salaries[emp_id].display()
        else:
            print("Not Found")
    elif choice == 4:
        break
