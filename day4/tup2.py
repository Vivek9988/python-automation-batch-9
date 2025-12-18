# 1. Empty tuple
tup = ()
print(tup)

# 2. Tuple using string values
tup = ('Geeks', "For")
print(tup)

# 3. Tuple using list (list to tuple conversion)
li = [1, 2, 4, 5, 6]
tup = tuple(li)
print(tup)

# 4. Tuple using built-in tuple() function with string
tup = tuple("Geeks")
print(tup)

# 5. Tuple with different data types
student = ("Bro", 21, "male")
print(student)

# Count element
print(student.count("Bro"))

# Find index of element
print(student.index("male"))

# Loop through tuple
for i in student:
    print(i)

# Check if element exists
if "Bro" in student:
    print("Bro is here!")
