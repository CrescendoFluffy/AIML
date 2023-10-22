# Write a code for removing the following elements from the set A={10, 15, 20, 25, 30}:
# (i) 25, (ii) 40, (iii) 10.

# Existing set A
A = {10, 15, 20, 25, 30}

# Remove 25 using discard() method
A.discard(25)

# Remove 40 using discard() method (no effect since 40 is not in the set)
A.discard(40)

# Remove 10 using discard() method
A.discard(10)

print("Updated set A:", A)