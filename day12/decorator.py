# decorator
def calculator(func):
    def wrapper(a, b):
        print("Calculating addition...")
        return a + b
    return wrapper


# using decorator
@calculator
def add(a, b):
    pass


# function call
result = add(10, 20)
print("Result:", result)
