# 2) a) Using laws of logics simplify the following networks shown in bel and �nd the Truth values by python

from sympy.logic.boolalg import Or, And, Not, Equivalent


def compound_prop(p, q):
    return Or(p, Not(q))


print("p q ans")
for p in [True, False]:
    for q in [True, False]:
        ans = compound_prop(p, q)
        print(p, q, ans)
