set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

union_set = set1 | set2

intersection_set = set1 & set2

difference_set = set1 - set2

sym_diff_set = set1 ^ set2

print("Set 1:", set1)
print("Set 2:", set2)

print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference (Set1 - Set2):", difference_set)
print("Symmetric Difference:", sym_diff_set)