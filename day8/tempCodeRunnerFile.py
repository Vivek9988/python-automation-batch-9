# ---------------- Student Class ----------------
class Student:
    def __init__(self, student_id, name, subjects, marks):
        self.student_id = student_id
        self.name = name
        self.subjects = subjects    # list of subject names
        self.marks = marks          # list of marks

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)

    def calculate_grade(self):
        avg = self.calculate_average()
        if avg >= 90:
            return "A+"
        elif avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 50:
            return "D"
        else:
            return "F"

    def display_details(self):
        print("\n----- Student Details -----")
        print("Student ID :", self.student_id)
        print("Name       :", self.name)
        print("\nSubjects & Marks:")
        for sub, mark in zip(self.subjects, self.marks):
            print(f"{sub} : {mark}")
        print("\nAverage Marks:", f"{self.calculate_average():.2f}")
        print("Grade        :", self.calculate_grade())


# ---------------- Main Program ----------------
print("Welcome to the Student Management System")

# -------- USER INPUT PART --------

# Get Student ID safely
while True:
    try:
        student_id = int(input("Enter Student ID: "))
        break
    except ValueError:
        print("Please enter a valid integer for Student ID.")

# Get Student Name
name = input("Enter Student Name: ")

# Get number of subjects safely
while True:
    try:
        n = int(input("Enter number of subjects: "))
        if n <= 0:
            print("Number of subjects must be greater than 0.")
            continue
        break
    except ValueError:
        print("Please enter a valid number for subjects.")

subjects = []
marks = []

for i in range(n):
    sub = input(f"Enter name of subject {i+1}: ")
    
    # Get marks safely
    while True:
        try:
            mark = int(input(f"Enter marks for {sub}: "))
            if mark < 0 or mark > 100:
                print("Marks should be between 0 and 100.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer for marks.")
    
    subjects.append(sub)
    marks.append(mark)

# Create Student object
student = Student(student_id, name, subjects, marks)

# Display details
student.display_details()
