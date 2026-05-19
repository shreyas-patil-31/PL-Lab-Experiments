# Tuple example

tup = (10, 20, 30, 40, 20)

print("Tuple:", tup)

# Access elements
print("First element:", tup[0])
print("Last element:", tup[-1])

# Length
print("Length:", len(tup))

# Count and index
print("Count of 20:", tup.count(20))
print("Index of 30:", tup.index(30))

# Traversing tuple
print("\nTraversing tuple:")
for i in tup:
    print(i, end=" ")

# Slicing
print("\n\nSlicing:")
print("First 3 elements:", tup[:3])
print("Last 2 elements:", tup[-2:])

# Concatenation
tup2 = (50, 60)
new_tup = tup + tup2
print("\nAfter concatenation:", new_tup)

# Repetition
print("Tuple repeated twice:", tup * 2)

# Membership
print("\nCheck if 20 is present:", 20 in tup)
print("Check if 99 is present:", 99 in tup)

# Max, Min, Sum
print("\nMaximum:", max(tup))
print("Minimum:", min(tup))
print("Sum:", sum(tup))

