# Write the python code for the following compound proposition:

# Define the boolean variables p, q, and r
p = True
q = False
r = True

# (i) p ∨ ¬q
prop_i = p or not q

# (ii) p → ¬q
prop_ii = not p or not q

# (iii) p → (p ∨ q)
prop_iii = not p or (p or q)

# (iv) p ∧ (¬p ∧ q)
prop_iv = p and (not p and q)

# (v) (p ∨ q) → r
prop_v = (p or q) or r

# (vi) {(p ∨ q) ∧ [(p → r) ∧ (q → r)]} → r
prop_vi = ((p or q) and ((not p or r) and (not q or r))) or r

# Print the results
print("(i) p ∨ ¬q:", prop_i)
print("(ii) p → ¬q:", prop_ii)
print("(iii) p → (p ∨ q):", prop_iii)
print("(iv) p ∧ (¬p ∧ q):", prop_iv)
print("(v) (p ∨ q) → r:", prop_v)
print("(vi) {{(p ∨ q) ∧ [(p → r) ∧ (q → r)]} → r:", prop_vi)
