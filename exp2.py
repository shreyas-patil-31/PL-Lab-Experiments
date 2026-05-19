# Program using if-else, loops, break, continue

num = int(input("Enter a number: "))

# If-elif-else
if num > 0:
    print("Number is Positive")
elif num == 0:
    print("Number is Zero")
else:
    print("Number is Negative")

# Check even/odd
if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# For loop
print("\nNumbers from 1 to 10:")
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# While loop
print("\nSum of first n numbers")
n = int(input("Enter n: "))
i = 1
sum_val = 0

while i <= n:
    sum_val += i
    i += 1

print("Sum:", sum_val)