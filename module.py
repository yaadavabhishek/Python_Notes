# ==========================================
# 📘 module.py
# ==========================================
# This file defines a collection of mathematical functions 
# that can be imported into another Python script.

# 1️⃣ Addition function
def add(a, b):
    """Returns the sum of a and b"""
    return a + b


# 2️⃣ Multiplication function
def multiply(a, b):
    """Returns the product of a and b"""
    return a * b


# 3️⃣ Subtraction function
def subtract(a, b):
    """Returns the result of a - b"""
    return a - b


# 4️⃣ Division function (with zero division check)
def divide(a, b):
    """Divides a by b. Returns an error message if b = 0"""
    if b == 0:
        return "❌ Error: Division by zero"
    return a / b


# 5️⃣ Square function
def square(x):
    """Returns the square of x"""
    return x ** 2


# 6️⃣ Power function
def power(base, exponent):
    """Returns base raised to the power of exponent"""
    return base ** exponent


# 7️⃣ Modulus function
def modulus(a, b):
    """Returns remainder when a is divided by b"""
    return a % b


# 8️⃣ Floor division function
def floor_divide(a, b):
    """Performs floor division (integer division)"""
    if b == 0:
        return "❌ Error: Division by zero"
    return a // b


# ✅ Example data (not necessary, but for reference)
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
