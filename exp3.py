# String operations demonstration

text = input("Enter a string: ")

print("\n--- BASIC OPERATIONS ---")
print("Original:", text)
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Length:", len(text))
print("Reversed:", text[::-1])

# Counting characters
char = input("Enter character to count: ")
print("Count:", text.count(char))

# Slicing
print("\n--- SLICING ---")
print("First 5 chars:", text[:5])
print("Last 5 chars:", text[-5:])

# Replace and split
print("\n--- MODIFYING STRING ---")
print("Replace 'a' with '@':", text.replace('a', '@'))
print("Split:", text.split())
