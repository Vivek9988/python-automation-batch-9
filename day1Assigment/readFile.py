# 5. Write a Python program to read and write files.

with open("myfile.txt", "w") as f:
    f.write("Hello, this is a sample text.\n")
    f.write("Writing to a file in Python.\n")


with open("myfile.txt", "r") as f:
    content = f.read()

print("File contents:\n")
print(content)
