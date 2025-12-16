# Function to take two numbers as input from the user
def get_numbers():
    # Input is taken as comma-separated values and converted to integers
    a, b = map(int, input("Enter two numbers (comma separated): ").split(","))
    return a, b


# Function to find the maximum of two numbers
def find_max(a, b):
    return max(a, b)


# Function to find the minimum of two numbers
def find_min(a, b):
    return min(a, b)


# Function to swap two numbers
def swap(a, b):
    return b, a


# Display menu options to the user
print("Get max, min or swap values")
print("1. Max")
print("2. Min")
print("3. Swap")

# Take input numbers
a, b = get_numbers()

# Take user's choice
choice = int(input("Enter your choice: "))

# Check the user's choice and perform the required operation
if choice == 1:
    # Print the maximum value
    print("Maximum value:", find_max(a, b))

elif choice == 2:
    # Print the minimum value
    print("Minimum value:", find_min(a, b))

elif choice == 3:
    # Swap the values and print them
    a, b = swap(a, b)
    print("After swapping:", a, b)

else:
    # Handle invalid choice
    print("Invalid choice")
