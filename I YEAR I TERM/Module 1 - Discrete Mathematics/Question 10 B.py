# Write a frozenset for any tuple and dictionary.
# Dictionary

# Create a dictionary
my_dict = {"apple": 3, "banana": 2, "cherry": 5, "date": 1}

# Convert the keys of the dictionary into a frozen set
my_frozen_set = frozenset(my_dict.keys())

# Print the frozen set
print(my_frozen_set)
