class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        print(f"Your balance is ₹{self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited. New balance: ₹{self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn. Remaining balance: ₹{self.balance}")
        else:
            print("Insufficient balance!")

    def menu(self):
        while True:
            print("\n--- ATM Menu ---")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.check_balance()
            elif choice == 2:
                amount = int(input("Enter amount to deposit: "))
                self.deposit(amount)
            elif choice == 3:
                amount = int(input("Enter amount to withdraw: "))
                self.withdraw(amount)
            elif choice == 4:
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")


# --- Main Program ---
atm = ATM(balance=10000)  # initial balance
atm.menu()
