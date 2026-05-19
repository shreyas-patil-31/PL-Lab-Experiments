# Exception handling example

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except ValueError:
    print("Error: Invalid input (only numbers allowed)")

finally:
    print("Program execution completed")

# Another example
try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError:
    print("Error: Index out of range")