# Tuple - ordered and unchangeable collection, used to group related data
student = ("Bro", 21, "male")

# Count occurrences of a value
print(student.count("Bro"))   # 1

# Get index of a value
print(student.index("male"))  # 2

# Loop through tuple
for i in student:
    print(i)

# Check if a value exists
if "Bro" in student:
    print("Bro is here!")
