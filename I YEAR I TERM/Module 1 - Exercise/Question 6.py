# Write a program to return a new set of identical items from two sets A and B
# A={10, 20, 30, 40, 50} and B={30, 40, 50, 60, 70}.

# Define sets A and B
A = {10, 20, 30, 40, 50}
B = {30, 40, 50, 60, 70}

# Find the identical items between sets A and B
common_items = A & B  # You can also use common_items = A.intersection(B)

# Print the common items
print("Identical items between sets A and B:", common_items)
