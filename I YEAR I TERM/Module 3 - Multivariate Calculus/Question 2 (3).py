# Compute the all first and second order derivative for the following function by using python:
# (iii) u=e^-x sint

import sympy as sp

# Define the variables
x, t = sp.symbols("x t")

# Define the function u(x, t)
u = sp.exp(-x) * sp.sin(t)

# Compute the first-order derivatives
du_dx = sp.diff(u, x)
du_dt = sp.diff(u, t)

# Compute the second-order derivatives
d2u_dx2 = sp.diff(du_dx, x)
d2u_dt2 = sp.diff(du_dt, t)
d2u_dxdt = sp.diff(du_dx, t)

# Print the results
print("First-order derivatives:")
print("du/dx =", du_dx)
print("du/dt =", du_dt)
print("\nSecond-order derivatives:")
print("d^2u/dx^2 =", d2u_dx2)
print("d^2u/dt^2 =", d2u_dt2)
print("d^2u/dxdt =", d2u_dxdt)
