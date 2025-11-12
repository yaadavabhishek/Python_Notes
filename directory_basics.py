# ================================================
# Python - Dictionaries (Key-Value Pairs)
# ================================================

print("----- Python Dictionaries Explained -----")

# ================================================
# A dictionary is used to store data values in key:value pairs.
# Dictionaries are ordered (Python 3.7+), changeable, and do not allow duplicates.
# ================================================

# Creating a Dictionary
student = {
    "name": "Abhishek",
    "age": 22,
    "course": "Data Analysis",
    "skills": ["Python", "NumPy", "Pandas"]
}

print("\nDictionary:", student)
print("Type:", type(student))

# ================================================
# Accessing Dictionary Items
# ================================================

print("\n----- Accessing Values -----")
print("Name:", student["name"])               # Access using key
print("Course:", student.get("course"))       # Using get() method
print("Skills:", student["skills"])           # List stored inside dictionary
print("First Skill:", student["skills"][0])   # Accessing list element inside dict

# ================================================
# Changing Values
# ================================================

print("\n----- Updating Values -----")
student["age"] = 23
print("Updated Age:", student["age"])

# Adding a new key-value pair
student["grade"] = "A"
print("Added Grade:", student)

# ================================================
# Looping through Dictionary
# ================================================

print("\n----- Looping through Dictionary -----")

# Loop through keys
for key in student:
    print("Key:", key)

# Loop through values
for value in student.values():
    print("Value:", value)

# Loop through both keys and values
for key, value in student.items():
    print(f"{key} → {value}")

# ================================================
# Check if a Key Exists
# ================================================

print("\n----- Check if Key Exists -----")
if "name" in student:
    print("Key 'name' found in dictionary!")

# ================================================
# Dictionary Length
# ================================================

print("\nTotal items in dictionary:", len(student))

# ================================================
# Remove Items from Dictionary
# ================================================

print("\n----- Removing Items -----")
student.pop("course")        # Removes an item by key
print("After pop():", student)

student.popitem()            # Removes the last inserted item
print("After popitem():", student)

# Delete specific key
del student["skills"]
print("After del:", student)

# Clear all items
student.clear()
print("After clear():", student)

# ================================================
# Nested Dictionaries
# ================================================

print("\n----- Nested Dictionaries -----")

students = {
    "student1": {"name": "Abhishek", "age": 22},
    "student2": {"name": "Yadav", "age": 23},
    "student3": {"name": "Ankit", "age": 21}
}

print("Nested Dictionary:", students)
print("Access nested value:", students["student1"]["name"])

# Loop through nested dictionary
for key, value in students.items():
    print(f"{key} → {value['name']} is {value['age']} years old")

# ================================================
# Useful Dictionary Methods
# ================================================

print("\n----- Useful Dictionary Methods -----")

person = {"name": "Abhishek", "age": 22, "city": "Noida"}

# copy()
copy_person = person.copy()
print("Copied dictionary:", copy_person)

# keys()
print("All keys:", person.keys())

# values()
print("All values:", person.values())

# items()
print("All key-value pairs:", person.items())

# update()
person.update({"country": "India"})
print("After update():", person)

# fromkeys()
keys = ("id", "name", "age")
default_value = None
new_dict = dict.fromkeys(keys, default_value)
print("fromkeys() result:", new_dict)

# setdefault()
print("setdefault():", person.setdefault("language", "Python"))
print("After setdefault():", person)

# ================================================
# Summary Table
# ================================================

# Method              | Description
# ---------------------------------------------------------
# dict.get(key)       | Returns value for the key
# dict.keys()         | Returns all keys
# dict.values()       | Returns all values
# dict.items()        | Returns all key-value pairs
# dict.update()       | Adds or updates items
# dict.pop(key)       | Removes specified key
# dict.popitem()      | Removes last inserted item
# dict.copy()         | Returns a shallow copy
# dict.clear()        | Removes all items
# dict.fromkeys()     | Creates a new dictionary with given keys
# dict.setdefault()   | Returns value if key exists, else adds with default

print("\n----- End of Python Dictionary Example -----")
