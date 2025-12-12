# 3. Create a calculator using Python functions.

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

print("Select operation: +  -  *  /")
op = input("Enter operator: ")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if op == '+':
    print("Result:", add(a, b))
elif op == '-':
    print("Result:", subtract(a, b))
elif op == '*':
    print("Result:", multiply(a, b))
elif op == '/':
    print("Result:", divide(a, b))
else:
    print("Invalid operator")