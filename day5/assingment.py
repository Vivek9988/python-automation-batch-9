# List of 20 students (First Name, Surname)
students = [
    ("Rahul", "Sharma"),
    ("Amit", "Kumar"),
    ("Priya", "Singh"),
    ("Rahul", "Verma"),
    ("Neha", "Gupta"),
    ("Amit", "Shah"),
    ("Rohit", "Yadav"),
    ("Anjali", "Mehra"),
    ("Vikas", "Patel"),
    ("Neha", "Malhotra"),
    ("Suman", "Das"),
    ("Karan", "Kapoor"),
    ("Pooja", "Jain"),
    ("Rohit", "Singh"),
    ("Manish", "Agarwal"),
    ("Sunita", "Rao"),
    ("Vikas", "Iyer"),
    ("Alok", "Mishra"),
    ("Pooja", "Bansal"),
    ("Deepak", "Chauhan")
]

# Dictionary to keep only one student per first name
unique_students = {}

# Set to track duplicate first names
duplicate_names = set()

for first_name, surname in students:
    if first_name in unique_students:
        duplicate_names.add(first_name)
    else:
        unique_students[first_name] = surname

# Final list with only one duplicate maintained
final_students = list(unique_students.items())

# Output
print("Final Students List (Only one duplicate maintained):\n")
for student in final_students:
    print(student)

print("\nDuplicate First Names Found:")
for name in duplicate_names:
    print(name)
