# what is the Cyclomatic Complexity
# Cyclomatic Complexity is a metric used in software testing and programming to measure:
# How complex a program or function is based on the number of decision points (if, else, loops, etc.)

# In simple words:

# It tells us how many independent paths are there in the code.

#Simple Formula

#Cyclomatic Complexity = Number of decision points + 1

# etc.
# Decision points are: if, else if, for, while, switch, case, 



def check_number(n):
    if n > 0:
        if n % 2 == 0:
            print("Positive Even")
        else:
            print("Positive Odd")
    elif n < 0:
        print("Negative")
    else:
        print("Zero")

# Apply Formula

# Cyclomatic Complexity = Decision Points + 1
# Cyclomatic Complexity = 3 + 1 = 4