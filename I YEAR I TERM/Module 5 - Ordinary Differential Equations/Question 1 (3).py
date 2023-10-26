# Solve the following differential equation by using Python
# (iii) (𝐷^2 + 𝐷)𝑦 = 𝑥^2 + 2𝑥 + 25

import sympy as sp

# Define the variables and the function
x = sp.symbols("x")
y = sp.Function("y")(x)

# Define the right-hand side of the equation
rhs = x**2 + 2 * x + 25

# Define the differential equation
diffeq = sp.Eq(y.diff(x, x) + y.diff(x), rhs)

# Solve the differential equation
solution = sp.dsolve(diffeq, y)

# Print the solution
print(solution)
