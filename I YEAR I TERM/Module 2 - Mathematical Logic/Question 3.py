# Test whether following is a valid argument or not by using python code
# If I Study, then I do not fail in the exam
# If I do not fail in the exam, then my father gifts a car to me
# ∴ If I study then my father gift me a car

from sympy import symbols, Implies, And, Not, simplify_logic

# Define symbolic variables
S = symbols("S")  # I study
F = symbols("F")  # I fail in the exam
C = symbols("C")  # My father gifts a car to me

# Define the premises and conclusion
premise1 = Implies(S, Not(F))  # S → ¬F
premise2 = Implies(Not(F), C)  # ¬F → C
conclusion = Implies(S, C)  # S → C

# Check the validity of the argument
validity = simplify_logic(And(premise1, premise2, Not(conclusion)))

if validity:
    print("The argument is valid. If I study, my father gifts me a car.")
else:
    print(
        "The argument is not valid. If I study, it does not guarantee my father gifts me a car."
    )
