# Write a frozenset for any tuple and dictionary.

# Create a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Convert the keys of the dictionary to a frozenset
frozen_set_from_dict_keys = frozenset(my_dict.keys())

# Print the frozenset
print("Frozen set from dictionary keys:", frozen_set_from_dict_keys)
