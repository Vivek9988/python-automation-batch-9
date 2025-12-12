# 2D LIST EXAMPLE IN PYTHON

# Individual lists
drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "hamburger", "hotdog"]
dessert = ["cake", "ice-cream"]

# Creating a 2D list (list inside list)
food = [drinks, dinner, dessert]

# Printing the entire 2D list
print("Full 2D list:")
print(food)

# Printing the individual list

print(food[0])




# Combine all lists into one large list
combined_food = drinks + dinner + dessert

print("\nConcatenated list (all items together):")

print(combined_food)
