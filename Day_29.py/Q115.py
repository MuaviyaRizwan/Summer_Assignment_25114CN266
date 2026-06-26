def string_operations():
    s = input("Enter a string: ")
    while True:
        print("\n--- String Operations Menu ---")
        print("1. Length of string")
        print("2. Reverse string")
        print("3. Count vowels")
        print("4. Convert to uppercase")
        print("5. Exit")
        
        choice = int(input("Enter choice: "))
        
        if choice == 1:
            print("Length =", len(s))
        elif choice == 2:
            print("Reversed =", s[::-1])
        elif choice == 3:
            vowels = "aeiouAEIOU"
            count = sum(1 for ch in s if ch in vowels)
            print("Vowel count =", count)
        elif choice == 4:
            print("Uppercase =", s.upper())
        elif choice == 5:
            print("Exiting String System...")
            break
        else:
            print("Invalid choice!")

string_operations()
