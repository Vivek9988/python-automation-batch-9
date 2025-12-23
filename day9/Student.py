class Student:
    def __init__(self, student_id, name):
        self.__student_id = student_id
        self.__name = name

    def get_student_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name


# Number of students
n = int(input("Enter number of students: "))
students = []

# Input student details in one line
for i in range(n):
    user_input = input(f"Enter student ID and name for student {i+1} (space separated): ")
    sid, name = user_input.split()  # split by space
    students.append(Student(sid, name))

# Even IDs first
print("\nEven Student IDs (Participate First):")
for s in students:
    num = int(s.get_student_id().split("_")[1])
    if num % 2 == 0:
        print(s.get_student_id(), s.get_name())

# Odd IDs later
print("\nOdd Student IDs (Participate Later):")
for s in students:
    num = int(s.get_student_id().split("_")[1])
    if num % 2 != 0:
        print(s.get_student_id(), s.get_name())
