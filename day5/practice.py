# Create dictionary
name_dict = {}

# Fill the dictionary
for first_name, last_name in student_names:
    if first_name not in name_dict:
        name_dict[first_name] = []
    name_dict[first_name].append(last_name)

# Show dictionary contents
for first_name in name_dict:
    print(first_name, len(name_dict[first_name]))

# Filter names with more than one surname
for first_name in name_dict:
    if len(name_dict[first_name]) > 1:
        print(
            "There are %d students having first name %s"
            % (len(name_dict[first_name]), first_name)
        )