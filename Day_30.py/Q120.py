def student_module(students):
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    students.append({"name": name, "roll": roll})

def book_module(library):
    book = input("Enter book title: ")
    library[book] = "Available"

def employee_module(employees):
    name = input("Enter employee name: ")
    emp_id = input("Enter employee ID: ")
    employees.append({"name": name, "id": emp_id})

def mini_project():
    students, library, employees = [], {}, []
    while True:
        print("\n--- Mini Project Menu ---")
        print("1. Add Student")
        print("2. Add Book")
        print("3. Add Employee")
        print("4. Display All Records")
        print("5. Exit")
        
        choice = int(input("Enter choice: "))
        
        if choice == 1:
            student_module(students)
        elif choice == 2:
            book_module(library)
        elif choice == 3:
            employee_module(employees)
        elif choice == 4:
            print("\nStudents:", students)
            print("Library:", library)
            print("Employees:", employees)
        elif choice == 5:
            print("Exiting Mini Project...")
            break
        else:
            print("Invalid choice!")

mini_project()
