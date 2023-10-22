# Write a program to add all its elements of A and B into a single set C
# A={"Yellow", "Orange", "Black"} and B={"Blue", "Green", "Red“}.

# Define sets A and B
A = {"Yellow", "Orange", "Black"}
B = {"Blue", "Green", "Red"}

# Create set C by combining A and B
C = A | B  # You can also use C = A.union(B)

# Print set C
print("Set C:", C)