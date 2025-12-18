# Introduction to Scripting
# This script shows how Python scripting works step by step


# Printing the purpose of the script
# Python scripts are executed line by line (interpreted language)


# =========================================================
# Python Variables, Datatypes, Keywords, Comments
# =========================================================


# Taking name input from the user (string by default)
name = input("Enter your name: ")


# Taking age input and converting it into integer using type casting
age = int(input("Enter your age: "))


# Taking salary input and converting it into float
salary = float(input("Enter your salary: "))


# Taking yes/no input, converting it to lowercase and checking condition
# Result will be True or False (Boolean)
is_employee = input("Are you an employee? (yes/no): ").lower() == "yes"


# Printing a heading for datatype display
print("\n--- Basic Datatypes ---")


# Printing name and its datatype
print("Name:", name, "| Type:", type(name))


# Printing age and its datatype
print("Age:", age, "| Type:", type(age))


# Printing salary and its datatype
print("Salary:", salary, "| Type:", type(salary))


# Printing employee status and its datatype
print("Is Employee:", is_employee, "| Type:", type(is_employee))


# =========================================================
# Type Conversion (Casting)
# =========================================================


# Printing section heading
print("\n--- Type Conversion ---")


# Converting integer age into float
age_float = float(age)


# Converting float salary into integer
salary_int = int(salary)


# Displaying converted values
print("Age converted to float:", age_float)
print("Salary converted to int:", salary_int)


# =========================================================
# Python Operators
# =========================================================


# Printing operators section heading
print("\n--- Operators ---")


# Taking first number input
a = int(input("Enter first number: "))


# Taking second number input
b = int(input("Enter second number: "))


# Arithmetic operators
print("Addition:", a + b)        # Adds two numbers
print("Subtraction:", a - b)     # Subtracts b from a
print("Multiplication:", a * b)  # Multiplies two numbers
print("Division:", a / b)        # Divides a by b


# Comparison operators
print("a > b:", a > b)           # Checks if a is greater than b
print("a == b:", a == b)         # Checks if a is equal to b


# Logical operator
print("a > 0 and b > 0:", a > 0 and b > 0)  # Logical AND


# Bitwise operator
print("Bitwise AND:", a & b)     # Bitwise AND operation


# =========================================================
# Python Control Statements (if, elif, else)
# =========================================================


# Printing conditional statements section heading
print("\n--- Conditional Statements ---")


# Checking age using if-elif-else
if age < 18:
   print("You are a minor.")     # Executed if condition is true
elif age >= 18 and age < 60:
   print("You are an adult.")    # Executed if above condition is false
else:
   print("You are a senior citizen.")  # Executed if all above are false


# Nested if condition
# Checking if user is an employee
if is_employee:
  
   # Checking salary inside employee condition
   if salary > 50000:
       print("High salary employee")
   else:
       print("Regular salary employee")


# =========================================================
# Python Loop Control Statements
# =========================================================


# For loop demonstration
print("\n--- For Loop ---")


# Taking number input
n = int(input("Enter a number to print numbers from 1 to n: "))


# Looping from 1 to n using range
for i in range(1, n + 1):
   print(i, end=" ")   # Printing values in same line


# Printing new line
print()


# While loop demonstration
print("\n--- While Loop ---")


# Initializing counter variable
count = 1


# While loop runs until condition becomes false
while count <= 5:
   print("Count:", count)  # Printing count value
   count += 1              # Incrementing counter


# =========================================================
# break, continue, pass
# =========================================================


# Printing loop control keywords section
print("\n--- break, continue, pass ---")


# For loop with break and continue
for i in range(1, 6):
  
   # Skips iteration when i equals 3
   if i == 3:
       continue
  
   # Stops loop completely when i equals 5
   if i == 5:
       break
  
   # Prints value of i
   print(i)


# Using pass as a placeholder
for _ in range(2):
   pass  # Does nothing


# =========================================================
# 2D List (List of Lists)
# =========================================================


# Printing 2D list section heading
print("\n--- 2D List ---")


# Taking number of rows
rows = int(input("Enter number of rows: "))


# Taking number of columns
cols = int(input("Enter number of columns: "))


# Creating empty matrix
matrix = []


# Outer loop for rows
for i in range(rows):
   row = []   # Creating empty row
  
   # Inner loop for columns
   for j in range(cols):
       value = int(input(f"Enter element [{i}][{j}]: "))
       row.append(value)  # Adding value to row
  
   matrix.append(row)     # Adding row to matrix


# Printing the 2D list
print("2D List (Matrix):")
for row in matrix:
   print(row)


# =========================================================
# Formatting Output
# =========================================================


# Printing formatted output section
print("\n--- Formatted Output ---")


# Using format() method
print("Hello {}, you are {} years old and earn {:.2f}".format(name, age, salary))


# Using f-string formatting
print(f"Name: {name}, Age: {age}, Salary: {salary}")


# =========================================================
# End of Script
# =========================================================


# Printing successful execution message
print("\nScript executed successfully.")