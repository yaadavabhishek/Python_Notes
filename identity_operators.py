# ================================================
# Python - Identity Operators Explained
# ================================================

print("----- Identity Operators in Python -----")

# Identity operators are used to compare the memory locations (object identity)
# They do NOT compare values directly, but whether two variables point to the same object in memory.

# There are two identity operators:
# 1. is      → Returns True if both variables point to the same object
# 2. is not  → Returns True if they point to different objects

# Example 1: Simple comparison
x = ["apple", "banana", "cherry"]
y = ["apple", "banana", "cherry"]
z = x

# 'is' checks whether x and y are the same object (same memory address)
print("x is y:", x is y)   # False → different lists in memory even if values are same

# '==' checks if values are equal (not identity)
print("x == y:", x == y)   # True → because contents are the same

# 'is' → True because z points to same object as x
print("x is z:", x is z)   # True → same memory object

# 'is not' → True if they are not same object
print("x is not y:", x is not y)  # True → different objects

# ================================================
# Checking Object IDs
# ================================================
print("\nObject IDs (Memory Addresses):")
print("id(x):", id(x))
print("id(y):", id(y))
print("id(z):", id(z))

# Different IDs → different objects
# Same IDs → same object reference

# ================================================
# Example: Immutable Objects (like integers, strings)
# ================================================

a = 10
b = 10
print("\na is b:", a is b)  # True → because Python caches small integers

a_str = "Hello"
b_str = "Hello"
print("a_str is b_str:", a_str is b_str)  # True → Python optimizes string literals

# ================================================
# Summary
# ================================================
# 'is'     → True if both refer to the same object in memory
# 'is not' → True if they refer to different objects

print("\n----- End of Identity Operators Example -----")
