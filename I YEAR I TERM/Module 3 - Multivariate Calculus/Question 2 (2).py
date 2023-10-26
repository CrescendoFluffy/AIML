# Compute the all first and second order derivative for the following function by using python:
# (ii)z=x/(x + y)

import sympy as sp

# Define the variables
x, y = sp.symbols("x y")

# Define the function z(x, y)
z = x / (x + y)

# Compute the first-order derivatives
dz_dx = sp.diff(z, x)
dz_dy = sp.diff(z, y)

# Compute the second-order derivatives
d2z_dx2 = sp.diff(dz_dx, x)
d2z_dy2 = sp.diff(dz_dy, y)
d2z_dxdy = sp.diff(dz_dx, y)

# Print the results
print("First-order derivatives:")
print("dz/dx =", dz_dx)
print("dz/dy =", dz_dy)
print("\nSecond-order derivatives:")
print("d^2z/dx^2 =", d2z_dx2)
print("d^2z/dy^2 =", d2z_dy2)
print("d^2z/dxdy =", d2z_dxdy)
