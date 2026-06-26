def inventory_system():
    inventory = {}
    while True:
        print("\n--- Inventory Management Menu ---")
        print("1. Add item")
        print("2. Update quantity")
        print("3. Display inventory")
        print("4. Delete item")
        print("5. Exit")
        
        choice = int(input("Enter choice: "))
        
        if choice == 1:
            item = input("Enter item name: ")
            qty = int(input("Enter quantity: "))
            inventory[item] = qty
        elif choice == 2:
            item = input("Enter item name: ")
            if item in inventory:
                qty = int(input("Enter new quantity: "))
                inventory[item] = qty
            else:
                print("Item not found!")
        elif choice == 3:
            print("Inventory:", inventory)
        elif choice == 4:
            item = input("Enter item name to delete: ")
            if item in inventory:
                del inventory[item]
            else:
                print("Item not found!")
        elif choice == 5:
            print("Exiting Inventory System...")
            break
        else:
            print("Invalid choice!")

inventory_system()
