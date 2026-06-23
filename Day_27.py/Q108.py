class Marksheet:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.total = sum(marks)
        self.percentage = self.total / len(marks)

    def display(self):
        print(f"Roll: {self.roll}, Name: {self.name}, Total: {self.total}, %: {self.percentage:.2f}")

marksheets = []

while True:
    print("\n1. Add Marksheet\n2. Display Marksheets\n3. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        roll = input("Enter Roll No: ")
        name = input("Enter Name: ")
        marks = []
        for i in range(3):  # 3 subjects
            marks.append(int(input(f"Enter marks for subject {i+1}: ")))
        marksheets.append(Marksheet(roll, name, marks))
    elif choice == 2:
        for m in marksheets:
            m.display()
    else:
        break
