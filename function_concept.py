# ==========================================================
# Python - User Input, Functions & Methods Explained Clearly
# ==========================================================

# ==============================
# 🧩 1. Basic User Input Example
# ==============================

print("\n----- User Input Example -----")

# The input() function takes user input as a STRING by default.
x = input('Enter x value: ')
y = input('Enter y value: ')

# Since input is string type, + concatenates (joins) the two strings.
print(f'Sum of {x} and {y} is: {x + y}')  # Example: if x=2, y=3 → Output: 23

# ----------------------------------
# Convert inputs to integers for math
# ----------------------------------

print("\n----- Converting Input to Integers -----")

x = int(input('Enter first number: '))
y = int(input('Enter second number: '))
print(f'Sum of {x} and {y} is: {x + y}')  # Example: 2 + 3 = 5


# ====================================
# 🌡️ 2. Temperature Conversion Example
# ====================================

print("\n----- Temperature Conversion Example -----")

# Formula: Fahrenheit = (9/5) * Celsius + 32
cel = float(input("Enter temperature in Celsius: "))
fer = (9/5) * cel + 32
print(f"{cel}° Celsius is equal to {fer}° Fahrenheit.")


# ==========================================
# ⏱️ 3. Time Conversion (Minutes → Seconds)
# ==========================================

print("\n----- Time Conversion Example -----")

m = int(input("Enter the number of minutes: "))
s = int(input("Enter the number of seconds: "))

# Formula: Total seconds = (minutes × 60) + seconds
total_seconds = m * 60 + s
print(f"Total time in seconds: {total_seconds} seconds")


# =====================================
# ⚙️ 4. Functions in Python (Basic Use)
# =====================================

print("\n----- Defining and Calling Functions -----")

def add(a, b):
    """This function adds two numbers and returns the result."""
    return a + b

# Calling the function
result = add(5, 10)
print(f"Result of add(5, 10): {result}")


# ====================================================
# 🧮 5. Function with Parameters (and User Input)
# ====================================================

print("\n----- Function with Parameters Example -----")

def add_numbers(a, b):
    """Takes two numbers and prints their sum."""
    c = a + b
    print(f"The sum of {a} and {b} is: {c}")

# Taking input from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Calling function
add_numbers(a, b)


# ====================================================
# 🔁 6. Function Returning a Value
# ====================================================

print("\n----- Function Returning a Value -----")

def multiply(x, y):
    """Returns the product of two numbers."""
    return x * y

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
product = multiply(num1, num2)
print(f"The product of {num1} and {num2} is: {product}")


# ====================================================
# 🎯 7. Function with Default Parameters
# ====================================================

def add(a, b=0):
    """Adds two numbers, with a default value for b."""
    c = a + b
    print(f"Sum is: {c}")

a = int(input("Enter first number: "))
b = int(input("Enter second number (or press Enter to use default 0): ") or 0)
add(a, b)


# ====================================================
# 🌡️ 8. Function Example - Conversion Utilities
# ====================================================

def convert_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit and returns result."""
    return (9/5) * celsius + 32

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = convert_to_fahrenheit(celsius)
print(f"{celsius}° Celsius is equal to {fahrenheit}° Fahrenheit.")


def convert_to_seconds(minutes, seconds):
    """Converts minutes and seconds into total seconds."""
    return (minutes * 60) + seconds

minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))
total_seconds = convert_to_seconds(minutes, seconds)
print(f"Total time in seconds: {total_seconds} seconds")


# ====================================================
# 🚫 9. Division Function with Error Handling
# ====================================================

print("\n----- Division Function with Zero Division Handling -----")

def divide(a, b):
    """Divides two numbers safely with zero division check."""
    if b == 0:
        return "⚠️ Division by zero is not allowed!"
    else:
        return a / b

num1 = int(input("Enter numerator: "))
num2 = int(input("Enter denominator: "))
result = divide(num1, num2)
print(f"Result of division: {result}")


# ====================================================
# 🧱 10. Class and Methods Example
# ====================================================

print("\n----- Class Method Example -----")

class Calculator:
    """A simple calculator class demonstrating methods."""

    def add(self, a, b):
        """Returns the sum of two numbers."""
        return a + b

    def subtract(self, a, b):
        """Returns the difference between two numbers."""
        return a - b

    def multiply(self, a, b):
        """Returns the product of two numbers."""
        return a * b

    def divide(self, a, b):
        """Handles division safely."""
        return "Cannot divide by zero" if b == 0 else a / b


# Create object of Calculator
calc = Calculator()

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"Addition: {calc.add(num1, num2)}")
print(f"Subtraction: {calc.subtract(num1, num2)}")
print(f"Multiplication: {calc.multiply(num1, num2)}")
print(f"Division: {calc.divide(num1, num2)}")


# ====================================================
# 🧠 Notes: Common Built-in Functions & Methods
# ====================================================

"""
🔹 Common Built-in Functions:
    - input()      → Takes input from the user
    - print()      → Displays output on screen
    - int(), float(), str() → Type conversions
    - len()        → Returns length of an object
    - type()       → Returns type of variable
    - range()      → Generates a sequence of numbers
    - max(), min() → Returns maximum/minimum value
    - sum()        → Sums up elements in a list or tuple
    - sorted()     → Returns sorted version of iterable

🔹 Common String Methods:
    - lower(), upper() → Change case
    - strip()          → Removes spaces
    - replace()        → Replace substring
    - split(), join()  → Convert between strings and lists
    - find()           → Find position of substring

🔹 Common List Methods:
    - append(), extend(), insert()
    - remove(), pop(), clear()
    - sort(), reverse()

🔹 Common Dictionary Methods:
    - keys(), values(), items()
    - get(), update(), pop()

🔹 Common Set Methods:
    - add(), remove(), union(), intersection(), difference()
"""

# ====================================================
# ✅ End of File
# ====================================================
print("\n----- End of User Input, Function & Method Examples -----")
