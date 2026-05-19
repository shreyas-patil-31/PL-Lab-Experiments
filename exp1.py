# Demonstration of different data types and operators

# Taking inputs
num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
float_num = float(input("Enter a float number: "))
text = input("Enter a string: ")

# Data Types
print("\n--- DATA TYPES ---")
print("num1 type:", type(num1))
print("num2 type:", type(num2))
print("float_num type:", type(float_num))
print("text type:", type(text))

# Arithmetic Operators
print("\n--- ARITHMETIC OPERATIONS ---")
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2 if num2 != 0 else "Cannot divide by zero")
print("Modulus:", num1 % num2 if num2 != 0 else "Undefined")

# Relational Operators
print("\n--- RELATIONAL OPERATORS ---")
print("num1 > num2:", num1 > num2)
print("num1 < num2:", num1 < num2)
print("num1 == num2:", num1 == num2)
print("num1 != num2:", num1 != num2)

# Logical Operators
print("\n--- LOGICAL OPERATORS ---")
print("(num1 > 0 and num2 > 0):", num1 > 0 and num2 > 0)
print("(num1 > 0 or num2 > 0):", num1 > 0 or num2 > 0)
print("not(num1 > num2):", not(num1 > num2))
