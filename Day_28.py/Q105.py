class Student:
    def __init__(self, roll, name, course):
        self.roll = roll
        self.name = name
        self.course = course

    def display(self):
        print(f"Roll: {self.roll}, Name: {self.name}, Course: {self.course}")

students = {}

while True:
    print("\n1. Add Student\n2. Display All\n3. Search by Roll\n4. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        roll = input("Enter Roll No: ")
        name = input("Enter Name: ")
        course = input("Enter Course: ")
        students[roll] = Student(roll, name, course)
    elif choice == 2:
        for s in students.values():
            s.display()
    elif choice == 3:
        roll = input("Enter Roll No: ")
        if roll in students:
            students[roll].display()
        else:
            print("Not Found")
    elif choice == 4:
        break
