# File handling example

# Writing to file
file = open("sample.txt", "w")
file.write("Hello, this is a file handling example.\n")
file.write("Python makes file handling easy.\n")
file.write("Also, Shreyas is a nice guy!.\n")
file.close()

# Reading file
file = open("sample.txt", "r")
print("\nFile Content:")
print(file.read())
file.close()

# Appending to file
file = open("sample.txt", "a")
file.write("This line is added later by Shreyas!.\n")
file.close()

# Reading line by line
file = open("sample.txt", "r")
print("\nReading line by line:")
for line in file:
    print(line.strip())
file.close()