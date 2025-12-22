# Function to calculate Simple Interest
def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100


# Taking inputs from the user
principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest: "))
time = float(input("Enter Time (in years): "))

# Calling the function
simple_interest = calculate_simple_interest(principal, rate, time)

# Displaying the result
print("Simple Interest is:", simple_interest)