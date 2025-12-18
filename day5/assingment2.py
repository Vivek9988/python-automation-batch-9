# Function 1: Calculator
def calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "sub":
        return a - b
    elif operation == "mul":
        return a * b
    elif operation == "div":
        if b != 0:
            return a / b
        else:
            return "Division by zero not allowed"
    else:
        return "Invalid operation"


# Function 2: Pass / Fail checker and the pass checker
def is_pass(marks):
    if marks >= 40:
        return True    # Pass
    else:
        return False   # Fail


# ------------------ Function Calls ------------------

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Enter operation (add/sub/mul/div): ")

outcome = calculator(a, b, operation)
print("Result:", outcome)


marks = int(input("Enter marks: "))

result = is_pass(marks)

# Catch True / False and print message
if result:
    print("Pass")
else:
    print("Fail")