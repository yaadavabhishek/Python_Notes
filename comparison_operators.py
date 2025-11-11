# ================================================
# Python - Comparison Operators Explained
# ================================================

print("----- Comparison Operators in Python -----")

# Comparison operators are used to compare two values.
# They always return a Boolean value: True or False.

a = 10
b = 5

# Equal to (==)
print("Equal to (==):", a == b)   # False → 10 is not equal to 5

# Not equal to (!=)
print("Not equal to (!=):", a != b)  # True → 10 is not equal to 5

# Greater than (>)
print("Greater than (>):", a > b)   # True → 10 is greater than 5

# Less than (<)
print("Less than (<):", a < b)     # False → 10 is not less than 5

# Greater than or equal to (>=)
print("Greater than or equal to (>=):", a >= b)  # True → 10 is greater than 5

# Less than or equal to (<=)
print("Less than or equal to (<=):", a <= b)  # False → 10 is not less than or equal to 5


# ================================================
# Real-world Example for Comparison
# ================================================

age = 18

if age >= 18:
    print("You are eligible to vote!")  # This line will execute
else:
    print("You are not eligible to vote!")


# ================================================
# Comparison with Strings
# ================================================
# String comparisons are done lexicographically (by Unicode order)

print("\nString Comparisons:")
name1 = "Apple"
name2 = "Banana"
print("Is 'Apple' equal to 'Banana'? →", name1 == name2)  # False
print("Is 'Apple' less than 'Banana'? →", name1 < name2)  # True (A < B)


# ================================================
# Summary Table
# ================================================
# ==  → Equal to
# !=  → Not equal to
# >   → Greater than
# <   → Less than
# >=  → Greater than or equal to
# <=  → Less than or equal to

print("\n----- End of Comparison Operators Example -----")
