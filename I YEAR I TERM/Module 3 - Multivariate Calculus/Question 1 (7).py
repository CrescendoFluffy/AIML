# Compute the first order derivative for the following function by using python:
# (vii) w=√r^2+s^2+t^2

import sympy as sp

# Define the symbols
r, s, t = sp.symbols("r s t")

# Define the function
w = sp.sqrt(r**2 + s**2 + t**2)

# Calculate the first-order partial derivatives
dw_dr = sp.diff(w, r)
dw_ds = sp.diff(w, s)
dw_dt = sp.diff(w, t)

print("First-order derivative with respect to r:")
print(dw_dr)

print("First-order derivative with respect to s:")
print(dw_ds)

print("First-order derivative with respect to t:")
print(dw_dt)