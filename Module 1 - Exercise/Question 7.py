# Write a Python program to update the first set with items that exist only in the first set A and not in the
# second set B, where A={10, 20, 30} and B={20, 40, 50}.

# Define sets A and B
A = {10, 20, 30}
B = {20, 40, 50}

# Update set A with items that exist only in A and not in B
A.difference_update(B)

# Print the updated set A
print("Updated set A:", A)