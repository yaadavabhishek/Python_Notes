# ================================================
# Python - Operator Precedence Explained
# ================================================

print("----- Operator Precedence in Python -----")

# Operator Precedence means:
# When an expression contains multiple operators,
# Python decides which operation to perform first
# based on a predefined priority (called precedence).

# Example:
# Multiplication (*) has higher precedence than Addition (+)
result = 10 + 2 * 3
print("Result of 10 + 2 * 3 =", result)  # Output: 16 (2*3 = 6, then 10+6 = 16)


# ================================================
# Using Parentheses () to Control Precedence
# ================================================
# Parentheses can be used to override the default precedence order.

result2 = (10 + 2) * 3
print("Result of (10 + 2) * 3 =", result2)  # Output: 36


# ================================================
# Example with Multiple Operators
# ================================================
# The order of precedence in the expression:
#   1. Parentheses ()
#   2. Exponentiation (**)
#   3. Multiplication, Division, Floor Division, Modulus (*, /, //, %)
#   4. Addition and Subtraction (+, -)

result3 = 5 + 3 * 2 ** 2
# Step 1: 2 ** 2 = 4
# Step 2: 3 * 4 = 12
# Step 3: 5 + 12 = 17
print("Result of 5 + 3 * 2 ** 2 =", result3)  # Output: 17


# ================================================
# Example Mixing Comparison and Arithmetic Operators
# ================================================
# Comparison operators are evaluated after arithmetic ones.

print("\nComparison with Arithmetic:")
result4 = 10 + 5 > 12
# Step 1: 10 + 5 = 15
# Step 2: 15 > 12 = True
print("Result of 10 + 5 > 12 =", result4)


# ================================================
# Logical Operators with Comparison
# ================================================
# Logical operators (and, or, not) have lower precedence than comparison operators.

print("\nLogical and Comparison Example:")
a = 10
b = 5
c = 20

result5 = a > b and c > a
# Step 1: a > b = True
# Step 2: c > a = True
# Step 3: True and True = True
print("Result of a > b and c > a =", result5)


# ================================================
# Example Showing NOT Operator Precedence
# ================================================
# 'not' has higher precedence than 'and' / 'or'

print("\nNOT Operator Precedence Example:")
x = True
y = False

result6 = not x or y
# Step 1: not x = False
# Step 2: False or False = False
print("Result of not x or y =", result6)


# ================================================
# Complete Operator Precedence Order (Highest → Lowest)
# ================================================
# 1. ()          → Parentheses
# 2. **          → Exponentiation
# 3. +x, -x, ~x  → Unary plus, minus, bitwise NOT
# 4. *, /, //, % → Multiplication, Division, Floor Div, Modulus
# 5. +, -        → Addition, Subtraction
# 6. <<, >>      → Bitwise shift operators
# 7. &           → Bitwise AND
# 8. ^, |        → Bitwise XOR, OR
# 9. ==, !=, >, <, >=, <= → Comparisons
# 10. is, is not, in, not in → Identity & Membership
# 11. not        → Logical NOT
# 12. and        → Logical AND
# 13. or         → Logical OR
# 14. =, +=, -=, *=, etc. → Assignment operators

print("\n----- Operator Precedence Order Displayed Above -----")


# ================================================
# Real-world Example
# ================================================

print("\nReal-world Example:")

marks = 85
attendance = 90

# A student passes only if marks >= 80 AND attendance >= 75
passed = marks >= 80 and attendance >= 75
print("Has the student passed?", passed)  # True

# Add parentheses to change logic
# Without parentheses → not is applied first
result7 = not marks < 80 and attendance > 70
print("Result of not marks < 80 and attendance > 70 =", result7)
# Step 1: marks < 80 → False
# Step 2: not False → True
# Step 3: True and True → True


print("\n----- End of Operator Precedence Example -----")
