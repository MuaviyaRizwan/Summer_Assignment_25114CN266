def array_operations():
    arr = []
    while True:
        print("\n--- Array Operations Menu ---")
        print("1. Insert element")
        print("2. Delete element")
        print("3. Display array")
        print("4. Search element")
        print("5. Exit")
        
        choice = int(input("Enter choice: "))
        
        if choice == 1:
            val = int(input("Enter element to insert: "))
            arr.append(val)
        elif choice == 2:
            val = int(input("Enter element to delete: "))
            if val in arr:
                arr.remove(val)
            else:
                print("Element not found!")
        elif choice == 3:
            print("Array:", arr)
        elif choice == 4:
            val = int(input("Enter element to search: "))
            if val in arr:
                print("Element found at index", arr.index(val))
            else:
                print("Element not found!")
        elif choice == 5:
            print("Exiting Array System...")
            break
        else:
            print("Invalid choice!")

array_operations()
