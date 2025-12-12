# 4. Write a program to count vowels in a string.

# 4. Write a program to count vowels in a string.
text = input("Enter a string: ")

vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Number of vowels:", count)