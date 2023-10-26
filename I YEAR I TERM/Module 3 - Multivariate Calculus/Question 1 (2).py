# Compute the first order derivative for the following function by using python:
# (ii) f(x, y)=x-y/x+y

import sympy as sp

# Define the symbols
x, y = sp.symbols("x y")

# Define the function
f = (x - y) / (x + y)

# Calculate the first-order partial derivatives
df_dx = sp.diff(f, x)
df_dy = sp.diff(f, y)

print("First-order derivative with respect to x:")
print(df_dx)

print("First-order derivative with respect to y:")
print(df_dy)
