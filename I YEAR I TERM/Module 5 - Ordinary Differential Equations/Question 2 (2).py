# Solve the following IVP by using Python
# (ii) 𝐷2 + 5𝐷 + 6 𝑦 = 𝑒𝑥, 𝑦 0 = 1, 𝑦′ 𝑜 = 2

import sympy as sp

# Define the variables and the function
x = sp.symbols("x")
y = sp.Function("y")(x)

# Define the right-hand side of the equation
rhs = sp.exp(x)

# Define the differential equation
diffeq = sp.Eq(y.diff(x, x) + 5 * y.diff(x) + 6 * y, rhs)

# Define the initial conditions
initial_conditions = {y.subs(x, 0): 1, y.diff(x).subs(x, 0): 2}

# Solve the differential equation with initial conditions
solution = sp.dsolve(diffeq, y, ics=initial_conditions)

# Print the solution
print(solution)
