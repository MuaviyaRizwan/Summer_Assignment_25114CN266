class Marksheet:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return self.total() / len(self.marks)

    def display(self):
        print(f"Roll: {self.roll}, Name: {self.name}, Total: {self.total()}, Percentage: {self.percentage():.2f}%")

marksheets = {}

while True:
    print("\n1. Add Marksheet\n2. Display All\n3. Search by Roll\n4. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        roll = input("Enter Roll No: ")
        name = input("Enter Name: ")
        marks = []
        for i in range(3):  # 3 subjects for simplicity
            marks.append(int(input(f"Enter marks for subject {i+1}: ")))
        marksheets[roll] = Marksheet(roll, name, marks)
    elif choice == 2:
        for m in marksheets.values():
            m.display()
    elif choice == 3:
        roll = input("Enter Roll No: ")
        if roll in marksheets:
            marksheets[roll].display()
        else:
            print("Not Found")
    elif choice == 4:
        break
