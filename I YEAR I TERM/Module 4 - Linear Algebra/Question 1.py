# Find all the eigenvalues and the corresponding eigenvectors of the matrix by using python
# 2 4
# 1 −3

import numpy as np

# Define the matrix
A = np.array([[2, 4], [1, -3]])

# Compute the eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)
