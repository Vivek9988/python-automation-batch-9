mylist = [1, 2, 3]
print("A list: %s" % mylist)

# List is used to store multiple items in a single variable
food = ["pizza", "hamburger", "hotdog", "spaghetti"]

# Access elements using index
print(food[0])   # pizza
print(food[3])   # spaghetti

# Update list element
food[0] = "sushi"
print(food[0])   # sushi

# Add item to the list
food.append("ice-cream")

# Remove a specific item
food.remove("hotdog")

# Remove last element
food.pop()

# Remove element by index
food.pop(1)

# Insert item at specific index
food.insert(0, "cake")

# Sort the list
food.sort()

# Print all items using loop
for i in food:
    print(i)

# Clear the list
food.clear()
