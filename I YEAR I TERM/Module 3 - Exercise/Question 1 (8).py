# Compute the first order derivative for the following function by using python:
# (viii) u = xe^-t sin theta

import sympy as sp

# Define the symbols
x, t, theta = sp.symbols("x t theta")

# Define the function
u = x * sp.exp(-t) * sp.sin(theta)

# Calculate the first-order partial derivatives
du_dx = sp.diff(u, x)
du_dt = sp.diff(u, t)
du_dtheta = sp.diff(u, theta)

print("First-order derivative with respect to x:")
print(du_dx)

print("First-order derivative with respect to t:")
print(du_dt)

print("First-order derivative with respect to theta:")
print(du_dtheta)
