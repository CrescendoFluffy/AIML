# Solve the following IVP by using Python
# (i) (𝐷^2 - 𝐷) 𝑦 = 𝑥^2 − 2𝑥 − 32, 𝑦(0) = 1,𝑦′(0) = −1

import sympy as sp

# Define the variables and the function
x = sp.symbols("x")
y = sp.Function("y")(x)

# Define the differential equation
diffeq = sp.Eq(y.diff(x, x) - y.diff(x), x**2 - 2 * x - 32)

# Define the initial conditions
initial_conditions = {y.subs(x, 0): 1, y.diff(x).subs(x, 0): -1}

# Solve the differential equation with initial conditions
solution = sp.dsolve(diffeq, y, ics=initial_conditions)

# Print the solution
print(solution)
