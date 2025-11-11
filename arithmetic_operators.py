# ================================================
# Python - Arithmetic Operators Explained
# ================================================

print("----- Arithmetic Operators in Python -----")

# Arithmetic operators are used to perform mathematical operations with numbers.

# Basic arithmetic operations
a = 10
b = 3

# Addition (+)
print("Addition:", a + b)   # 10 + 3 = 13

# Subtraction (-)
print("Subtraction:", a - b)  # 10 - 3 = 7

# Multiplication (*)
print("Multiplication:", a * b)  # 10 * 3 = 30

# Division (/) → Always returns a float
print("Division (/):", a / b)    # 10 / 3 = 3.3333333333333335

# Floor Division (//) → Returns an integer by rounding down
print("Floor Division (//):", a // b)  # 10 // 3 = 3
# Floor Division always rounds DOWN to the nearest integer.
# Example:
print("Floor Division (9 // 2):", 9 // 2)     # 4 (since 9/2 = 4.5 → rounded down)
print("Floor Division (-9 // 2):", -9 // 2)   # -5 (since it rounds DOWN to -5)

# Modulus (%) → Returns the remainder
print("Modulus (%):", a % b)   # 10 % 3 = 1 (remainder after division)

# Power Operator (**) → Used for exponents
print("Power (**):", a ** b)   # 10 ** 3 = 1000 (means 10³)

# Another example of power
print("2 ** 4 =", 2 ** 4)   # 2 * 2 * 2 * 2 = 16

# You can also use the pow() function (does the same as **)
print("pow(2, 4) =", pow(2, 4))  # Output: 16

# ================================================
# Real-world Examples
# ================================================

# 1. Average of two numbers
num1 = 15
num2 = 25
average = (num1 + num2) / 2
print("Average:", average)  # (15 + 25) / 2 = 20.0

# 2. Area of a circle (using power)
radius = 5
pi = 3.14159
area = pi * (radius ** 2)  # πr²
print("Area of Circle:", area)

# 3. Using Floor Division to convert seconds into minutes
seconds = 125
minutes = seconds // 60     # Full minutes
remaining_seconds = seconds % 60  # Remainder seconds
print(f"{seconds} seconds = {minutes} minute(s) and {remaining_seconds} second(s)")

print("\n----- End of Arithmetic Operators Example -----")
