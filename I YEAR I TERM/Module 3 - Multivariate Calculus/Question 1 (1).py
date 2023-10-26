# Compute the first order derivative for the following function by using python:
# (i) f(x, y) = x^5 + 3x^3y^2+3xy^4

import sympy as sp

x, y = sp.symbols("x y")
f = x**5 + 3 * x**3 * y**2 + 3 * x * y**4

df_dx = sp.diff(f, x)
df_dy = sp.diff(f, y)

print("First-order derivative with respect to x:")
print(df_dx)

print("First-order derivative with respect to y:")
print(df_dy)
