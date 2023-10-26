# Solve the following differential equation by using Python
# (v) (𝐷^4 − 18𝐷^2 + 18) 𝑦 = 36𝑒^3𝑥 + 8^𝑥

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


# Define the differential equation as a system of first-order ODEs
def system(x, z):
    y, yp, ypp, yppp = z
    dydx = [yp, ypp, yppp, 18 * ypp - 18 * y + 36 * np.exp(3 * x) + 8**x]
    return dydx


# Define the range of x values
x_span = (0, 1)

# Initial conditions for y and its derivatives
initial_conditions = [0, 0, 0, 0]

# Create a grid of x values
x_values = np.linspace(x_span[0], x_span[1], 100)

# Solve the system of ODEs numerically
solution = solve_ivp(system, x_span, initial_conditions, t_eval=x_values)

# Extract the solution for y
y_solution = solution.y[0]

# Plot the solution
plt.plot(x_values, y_solution)
plt.xlabel("x")
plt.ylabel("y(x)")
plt.title("Numerical Solution of the Differential Equation")
plt.grid(True)
plt.show()
