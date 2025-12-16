# Dictionary
# A changeable, unordered collection of unique key:value pairs
# Fast access because Python dictionaries use hashing

capitals = {
    'USA': "Washington DC",
    'India': "New Delhi",
    'China': "Beijing",
    'Russia': "Moscow"
}

# Accessing values
print(capitals['Russia'])        # Moscow
print(capitals.get('Germany'))   # None (key not present)

# Getting all keys
print(capitals.keys())           # dict_keys(['USA', 'India', 'China', 'Russia'])

# Getting all values
print(capitals.values())         # dict_values(['Washington DC', 'New Delhi', 'Beijing', 'Moscow'])

# Getting all key-value pairs
print(capitals.items())          # dict_items([('USA', 'Washington DC'), ('India', 'New Delhi'), ...])

# Updating dictionary
capitals.update({'Germany': "Berlin"})       # Add new key-value
capitals.update({'USA': "Las Vegas"})        # Update existing key

# Removing items
capitals.pop("China")                         # Removes China
# capitals.popitem()                         # Removes last inserted item (optional)

# Loop through dictionary
for key, value in capitals.items():
    print(key, ":", value)

# Clear dictionary
capitals.clear()
print("After clear:", capitals)            
