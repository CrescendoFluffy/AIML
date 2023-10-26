# Solve the following differential equation by using Python
# (i) (𝐷^3 − 5𝐷^2 + 7𝐷 − 3)y=0

import sympy as sp

# Define the variable and the function
x = sp.symbols("x")
y = sp.Function("y")(x)

# Define the differential equation
equation = sp.diff(y, x, x, x) - 5 * sp.diff(y, x, x) + 7 * sp.diff(y, x) - 3 * y

# Solve the differential equation
solution = sp.dsolve(equation, y)

# Print the solution
print("Solution:", solution)
