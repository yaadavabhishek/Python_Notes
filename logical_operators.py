# ================================================
# Python - Logical Operators Explained
# ================================================

print("----- Logical Operators in Python -----")

# Logical operators are used to combine multiple conditions.
# They return True or False depending on the logic applied.

# 'and' → Returns True only if BOTH conditions are True
x = 10

print("\nAND Operator:")
print(x > 5 and x < 20)   # True → both conditions True
print(x > 5 and x > 20)   # False → one condition False

# 'or' → Returns True if ANY one condition is True
print("\nOR Operator:")
print(x > 5 or x < 5)     # True → at least one condition True
print(x < 5 or x < 3)     # False → both conditions False

# 'not' → Reverses the Boolean result (True → False, False → True)
print("\nNOT Operator:")
print(not(x > 5))         # False → because x > 5 is True
print(not(x < 5))         # True  → because x < 5 is False


# ================================================
# Logical Operators with Real-World Conditions
# ================================================

print("\n----- Combining Logical Operators with Conditions -----")

# Example 1: Checking if a number is within a range
num = 15

if num > 10 and num < 20:
    print(f"{num} is between 10 and 20")
else:
    print(f"{num} is outside the range")

# Example 2: Using OR
user = "admin"
password = "1234"

if user == "admin" or password == "1234":
    print("Login Successful!")   # True because at least one condition is True
else:
    print("Login Failed!")

# Example 3: Using NOT
logged_in = False

if not logged_in:
    print("Please log in first!")  # True because not(False) = True


# ================================================
# Logical Operators with Lists
# ================================================
print("\nLogical Operators with Lists:")

list1 = [1, 2, 3]
list2 = []

print("list1 and list2 →", list1 and list2)  # [] because second is empty (False)
print("list1 or list2 →", list1 or list2)    # [1,2,3] because first is True
print("not list1 →", not list1)              # False because list1 is not empty


# ================================================
# Summary Table
# ================================================
# and → True if both conditions are True
# or  → True if at least one condition is True
# not → Reverses the Boolean result

print("\n----- End of Logical Operators Example -----")
