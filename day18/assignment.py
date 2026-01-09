# 1. Define cyclomatic complexity. Why is it important?
# ✅ Definition:

# Cyclomatic Complexity is a software metric used to measure the number of independent execution paths in a program.

# Why it is important:

# It tells us:

# 1.How complex the code is

# 2.How many test cases are needed

# 3.Which code is risky and hard to maintain

# 4.Higher complexity = more chances of bugs

# 2. Formula for Cyclomatic Complexity and explain each term

# 📌 Formula:

# V(G) = E − N + 2P

# Where:

# E = Number of edges in the control flow graph

# N = Number of nodes in the control flow graph

# P = Number of connected components (usually 1 for a single program)

# 👉 For most programs:

# V(G) = E − N + 2

# 3. Calculate CC for program with 10 nodes and 12 edges

# Given:

# N = 10

# E = 12

# P = 1

# ✅ Apply formula:

# V(G) = E − N + 2
# V(G) = 12 − 10 + 2 = 4

# ✔ Answer: Cyclomatic Complexity = 4
# 4. Cyclomatic complexity of program with 3 decision points
# 📌 Formula:

# CC = Decision points + 1

# So:

# CC = 3 + 1 = 4

# ✔ Answer: 4
# 5. How does cyclomatic complexity help in testing?

# It tells:

# Minimum number of test cases needed

# Number of independent paths

# Helps in:

# Path coverage

# Finding critical and risky code

# Better test planning

# 📌 One-line:

# Cyclomatic complexity helps testers decide the minimum number of test cases required for complete path coverage.

# 6. Limitations of cyclomatic complexity

# It:

# Measures only control flow, not logic quality

# Does not detect all bugs

# Does not consider data complexity

# Cannot measure code readability or performance

# 7. Compute CC for given pseudocode
# Given:
if A > 0:
    if B > 0:
        print("X")
    else:
        print("Y")



# 🔍 Decision points:

# IF A > 0

# IF B > 0

# Total decision points = 2

# 🧮 Formula:

# CC = Decision points + 1 = 2 + 1 = 3

# ✅ Final Answers Summary:
# Question	Answer
# Q1	CC = number of independent paths
# Q3	4
# Q4	4
# Q7	3