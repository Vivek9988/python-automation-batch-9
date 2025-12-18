# Set (duplicates automatically removed)
mySet = {"apple", "banana", "pomegranate", "apple", False, 2, 2}

# List
mylist = ['a', 'b']

# Another set
mySet2 = {"", "n"}

# Print list
print(mylist)

# Empty set and empty dictionary
empty_set = set()
empty_dict = {}

print(type(empty_set))   # <class 'set'>
print(type(empty_dict))  # <class 'dict'>

# Add and remove element in list
mylist.append(10)
mylist.remove(10)

# Update set using list
mySet.update(mylist)

# Length of set
count = len(mySet)
print("Length:", count)

# Union
print(mySet | mySet2)

# Intersection
print(mySet & mySet2)

# Loop through set
for fruit in mySet:
    print(fruit)

