# Test whether following is a valid argument or not by using python code
# If Sachin hits a century then he gets a free car
# Sachin hits a century
# ∴ sachin gets a free car

from sympy import symbols, Implies, And, Not, simplify_logic

# Define symbolic variables
sachin_hits_century = symbols('Sachin_hits_century')
sachin_gets_free_car = symbols('Sachin_gets_free_car')

# Define the premises and conclusion
premise1 = Implies(sachin_hits_century, sachin_gets_free_car)  # If Sachin hits a century, he gets a free car
premise2 = sachin_hits_century  # Sachin hits a century
conclusion = sachin_gets_free_car  # Sachin gets a free car

# Check the validity of the argument
validity = simplify_logic(And(premise1, premise2, Not(conclusion)))

if validity:
    print("The argument is valid. Sachin gets a free car.")
else:
    print("The argument is not valid. Sachin doesn't get a free car.")