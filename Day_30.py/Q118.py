def library_system():
    library = {}
    while True:
        print("\n--- Library Menu ---")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")
        
        choice = int(input("Enter choice: "))
        
        if choice == 1:
            book = input("Enter book title: ")
            library[book] = "Available"
        elif choice == 2:
            for b, status in library.items():
                print(f"{b} - {status}")
        elif choice == 3:
            book = input("Enter book title to issue: ")
            if book in library and library[book] == "Available":
                library[book] = "Issued"
                print("Book issued successfully!")
            else:
                print("Book not available!")
        elif choice == 4:
            book = input("Enter book title to return: ")
            if book in library and library[book] == "Issued":
                library[book] = "Available"
                print("Book returned successfully!")
            else:
                print("Invalid return!")
        elif choice == 5:
            break
        else:
            print("Invalid choice!")

library_system()
