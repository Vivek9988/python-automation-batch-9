# 2. Write a program to find the largest number in a list.
numbers = [10, 25, 4, 89, 56]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("The largest number is:", largest)