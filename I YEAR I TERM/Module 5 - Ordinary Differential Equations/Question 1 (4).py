# Solve the following differential equation by using Python
# (iv) (𝐷^2 + 4)𝑦 = 𝑒^4𝑥

import sympy as sp

# Define the variables and the function
x = sp.symbols("x")
y = sp.Function("y")(x)

# Define the right-hand side of the equation
rhs = sp.exp(4 * x)

# Define the differential equation
diffeq = sp.Eq(y.diff(x, x) + 4 * y, rhs)

# Solve the differential equation
solution = sp.dsolve(diffeq, y)

# Print the solution
print(solution)
