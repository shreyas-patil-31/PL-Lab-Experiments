# Functions example

# Function to add two numbers
def add(a, b):
    return a + b

# Function to check even/odd
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Function with default argument
def greet(name="Student"):
    print("Hello", name)

# Main program
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Sum:", add(x, y))

num = int(input("Enter number to check even/odd: "))
print("Result:", check_even_odd(num))
