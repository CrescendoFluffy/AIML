# Write a Python program to update set A by adding items from set B, except common items
# A={10, 20, 30, 40, 50} and B={30, 40, 50, 60, 70}.

# Define sets A and B
A = {10, 20, 30, 40, 50}
B = {30, 40, 50, 60, 70}

# Find the items in B that are not in A
items_to_add = B.difference(A)

# Update set A by adding the items from set B that are not in A
A.update(items_to_add)

# Print the updated set A
print("Updated set A:", A)
