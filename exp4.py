# List operations

lst = []

n = int(input("Enter number of elements: "))

for i in range(n):
    val = int(input("Enter element: "))
    lst.append(val)

print("\nOriginal List:", lst)

# Basic operations
lst.append(100)
print("After append:", lst)

lst.insert(1, 50)
print("After insert:", lst)

if len(lst) > 0:
    lst.pop()
print("After pop:", lst)

# Searching
search = int(input("Enter element to search: "))
if search in lst:
    print("Element found at index:", lst.index(search))
else:
    print("Element not found")

# Sorting
print("Sorted List:", sorted(lst))
print("Maximum:", max(lst))
print("Minimum:", min(lst))

# List comprehension
squares = [x**2 for x in lst]
print("Squares:", squares)