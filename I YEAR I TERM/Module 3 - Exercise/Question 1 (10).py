# Compute the first order derivative for the following function by using python:
# (x) f(x,t) = arctan(x√t)

import sympy as sp

# Define the symbols
x, t = sp.symbols("x t")

# Define the function
f = sp.atan(x * sp.sqrt(t))

# Calculate the first-order derivative
df_dx = sp.diff(f, x)

print("First-order derivative with respect to x:")
print(df_dx)
