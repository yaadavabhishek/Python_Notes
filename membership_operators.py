# ================================================
# Python - Membership Operators Explained
# ================================================

print("----- Membership Operators in Python -----")

# Membership operators test if a value or variable is found in a sequence (like list, string, tuple, etc.)

# There are two membership operators:
# 1. in      → Returns True if the value is present in the sequence
# 2. not in  → Returns True if the value is NOT present in the sequence

# Example 1: Using 'in'
fruits = ["apple", "banana", "cherry"]

print("'apple' in fruits:", "apple" in fruits)   # True → apple is in list
print("'mango' in fruits:", "mango" in fruits)   # False → mango not found

# Example 2: Using 'not in'
print("'mango' not in fruits:", "mango" not in fruits)  # True → mango not in list
print("'banana' not in fruits:", "banana" not in fruits) # False → banana exists

# ================================================
# Example with Strings
# ================================================
text = "Python programming is fun!"

print("\nString Membership:")
print("'Python' in text:", "Python" in text)    # True → substring exists
print("'java' in text:", "java" in text)        # False → case-sensitive
print("'Fun' in text:", "Fun" in text)          # False → case-sensitive
print("'fun' in text:", "fun" in text)          # True  → exact lowercase match

# ================================================
# Example with Tuples
# ================================================
numbers = (10, 20, 30, 40)

print("\nTuple Membership:")
print("20 in numbers:", 20 in numbers)   # True
print("50 not in numbers:", 50 not in numbers)  # True

# ================================================
# Example with Dictionary (checks keys only)
# ================================================
person = {"name": "Abhishek", "age": 25}

print("\nDictionary Membership:")
print("'name' in person:", "name" in person)   # True → key exists
print("'Abhishek' in person:", "Abhishek" in person)  # False → value not checked
print("'age' not in person:", "age" not in person)     # False → key exists

# ================================================
# Summary
# ================================================
# 'in'      → True if the element is found in the sequence
# 'not in'  → True if the element is NOT found in the sequence

print("\n----- End of Membership Operators Example -----")
