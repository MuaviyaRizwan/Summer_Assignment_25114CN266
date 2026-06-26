def employee_system():
    employees = []
    while True:
        print("\n--- Employee Management Menu ---")
        print("1. Add Employee")
        print("2. Display Employees")
        print("3. Search Employee by ID")
        print("4. Exit")
        
        choice = int(input("Enter choice: "))
        
        if choice == 1:
            name = input("Enter employee name: ")
            emp_id = input("Enter employee ID: ")
            employees.append({"name": name, "id": emp_id})
        elif choice == 2:
            for e in employees:
                print("Name:", e["name"], "| ID:", e["id"])
        elif choice == 3:
            search = input("Enter employee ID: ")
            found = [e for e in employees if e["id"] == search]
            if found:
                print("Found:", found[0])
            else:
                print("Employee not found!")
        elif choice == 4:
            break
        else:
            print("Invalid choice!")

employee_system()
