# Find all the eigenvalues and the corresponding eigenvectors of the matrix by using python
# 8 −6 2
# −6 7 −4
# 2 −4 3

import numpy as np

# Define the matrix
A = np.array([[8, -6, 2], [-6, 7, -4], [2, -4, 3]])

# Compute the eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)
