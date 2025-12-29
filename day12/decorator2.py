def calculator(func):
    def wrapper(a, b):
        print("Operation is starting...")
        result = func(a, b)
        print("Operation completed")
        return result
    return wrapper
@calculator
def add(a, b):
    return a + b


@calculator
def subtract(a, b):
    return a - b


@calculator
def multiply(a, b):
    return a * b

print(add(10, 5))
print(subtract(10, 5))
print(multiply(10, 5))
