# Solve the following differential equation by using Python
# (ii) (D^3-3D^2 + 3D-1)𝑦=0

import sympy as sp

# Define the variable
x = sp.symbols("x")

# Define the function
y = sp.Function("y")

# Define the differential equation
diffeq = sp.Eq(y(x).diff(x, x, x) - 3 * y(x).diff(x, x) + 3 * y(x).diff(x) - 1, 0)

# Solve the differential equation
solutions = sp.dsolve(diffeq)

# Print the solutions
print(solutions)
