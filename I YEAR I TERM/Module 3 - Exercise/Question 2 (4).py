# Compute the all first and second order derivative for the following function by using python:
# (iv) f(x, y) = ln(3x+5y)

import sympy as sp

# Define the variables
x, y = sp.symbols("x y")

# Define the function f(x, y)
f = sp.log(3 * x + 5 * y)

# Compute the first-order derivatives
df_dx = sp.diff(f, x)
df_dy = sp.diff(f, y)

# Compute the second-order derivatives
d2f_dx2 = sp.diff(df_dx, x)
d2f_dy2 = sp.diff(df_dy, y)
d2f_dxdy = sp.diff(df_dx, y)

# Print the results
print("First-order derivatives:")
print("df/dx =", df_dx)
print("df/dy =", df_dy)
print("\nSecond-order derivatives:")
print("d^2f/dx^2 =", d2f_dx2)
print("d^2f/dy^2 =", d2f_dy2)
print("d^2f/dxdy =", d2f_dxdy)
