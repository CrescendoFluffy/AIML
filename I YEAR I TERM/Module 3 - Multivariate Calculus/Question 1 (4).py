# Compute the first order derivative for the following function by using python:
# (iv) w = ln(x+2y+3z)

import sympy as sp

# Define the symbols
x, y, z = sp.symbols("x y z")

# Define the function
w = sp.log(x + 2 * y + 3 * z)

# Calculate the first-order partial derivatives
dw_dx = sp.diff(w, x)
dw_dy = sp.diff(w, y)
dw_dz = sp.diff(w, z)

print("First-order derivative with respect to x:")
print(dw_dx)

print("First-order derivative with respect to y:")
print(dw_dy)

print("First-order derivative with respect to z:")
print(dw_dz)