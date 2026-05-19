# Dictionary example

student = {
    "name": "Shreyas",
    "age": 20,
    "marks": 85
}

print("Dictionary:", student)

# Access values
print("Name:", student["name"])
print("Marks:", student["marks"])

# Update value
student["marks"] = 90
print("Updated marks:", student["marks"])

# Add new key
student["city"] = "Pune"
print("After adding city:", student)

# Loop through dictionary
print("\nAll details:")
for key, value in student.items():
    print(key, ":", value)