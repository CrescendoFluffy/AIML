# Compute the all first and second order derivative for the following function by using python:
# (vi) v=√x^2 + y^2

import sympy as sp

# Define the variables
x, y = sp.symbols("x y")

# Define the function v(x, y)
v = sp.sqrt(x**2 + y**2)

# Compute the first-order derivatives
dv_dx = sp.diff(v, x)
dv_dy = sp.diff(v, y)

# Compute the second-order derivatives
d2v_dx2 = sp.diff(dv_dx, x)
d2v_dy2 = sp.diff(dv_dy, y)
d2v_dxdy = sp.diff(dv_dx, y)

# Print the results
print("First-order derivatives:")
print("dv/dx =", dv_dx)
print("dv/dy =", dv_dy)
print("\nSecond-order derivatives:")
print("d^2v/dx^2 =", d2v_dx2)
print("d^2v/dy^2 =", d2v_dy2)
print("d^2v/dxdy =", d2v_dxdy)
