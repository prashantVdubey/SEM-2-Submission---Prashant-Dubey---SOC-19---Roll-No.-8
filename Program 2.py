# Experiment 2: Set Operations

# 1. Create and Access
set_a = {10, 20, 30, 40, 50}
set_b = {30, 40, 50, 60, 70}
print('Set A:', set_a)
print('Set B:', set_b)

# Check membership
print('Is 20 in set_a?', 20 in set_a)
print('Is 60 in set_a?', 60 in set_a)

# 2. Union
union_set = set_a | set_b
print('\nUnion (A | B):', union_set)

# 3. Intersection
intersection_set = set_a & set_b
print('Intersection (A & B):', intersection_set)

# 4. Difference
diff_a_b = set_a - set_b
diff_b_a = set_b - set_a
print('Difference (A - B):', diff_a_b)
print('Difference (B - A):', diff_b_a)

# Symmetric Difference
sym_diff = set_a ^ set_b
print('Symmetric Difference (A ^ B):', sym_diff)
