def student_record_system():
    students = []
    while True:
        print("\n--- Student Record Menu ---")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student by Name")
        print("4. Exit")
        
        choice = int(input("Enter choice: "))
        
        if choice == 1:
            name = input("Enter student name: ")
            roll = input("Enter roll number: ")
            students.append({"name": name, "roll": roll})
        elif choice == 2:
            for s in students:
                print("Name:", s["name"], "| Roll:", s["roll"])
        elif choice == 3:
            search = input("Enter name to search: ")
            found = [s for s in students if s["name"].lower() == search.lower()]
            if found:
                print("Found:", found[0])
            else:
                print("Student not found!")
        elif choice == 4:
            break
        else:
            print("Invalid choice!")

student_record_system()
