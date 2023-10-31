# 2) a) Using laws of logics simplify the following networks shown in bel and �nd the Truth values by python

from sympy.logic.boolalg import Or, And, Not, Equivalent


def compound_prop(p, t):
    return And(p, t)


print("p t ans")
for p in [True, False]:
    for t in [True, False]:
        ans = compound_prop(p, t)
        print(p, t, ans)
