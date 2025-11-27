# ==========================================================
#  Python Exception & Error Handling Examples
# ==========================================================

# -------------------------------
# 🧠 What is an Error?
# -------------------------------
# Errors are problems that stop program execution.
# Two major types:
#   1. Syntax Errors → Detected before code runs (compile-time)
#   2. Exceptions → Detected during execution (runtime)
#
# Exception handling prevents your program from crashing.


# ==========================================================
# 0️⃣ Indentation Error Example
# ==========================================================
print("\n----- Indentation Error Example -----")

# IndentationError occurs when Python code is not properly aligned.
# Python uses indentation (spaces/tabs) to define code blocks like loops, if-statements, or functions.
# Uncomment the following lines to see the error in VS Code.

"""
# ❌ Example of IndentationError
def greet():
print("Hello, World!")   # This line should be indented

# Output:
# IndentationError: expected an indented block after function definition on line X
"""

# ✅ Correct version
def greet():
    print("Hello, World!")  # Proper indentation inside function

greet()


# ==========================================================
# 1️⃣ Syntax Error Example (Uncomment to See)
# ==========================================================
# print("Hello World"     # ❌ Missing closing parenthesis -> SyntaxError
# Output: SyntaxError: '(' was never closed


# ==========================================================
# 2️⃣ Example of a Runtime Error (Handled)
# ==========================================================
print("\n----- Runtime Error Example -----")

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"Result = {result}")
except ZeroDivisionError:
    print("⚠️ Error: Cannot divide by zero.")
except ValueError:
    print("⚠️ Error: Please enter a valid number.")
except Exception as e:
    print(f"⚠️ Unexpected error: {e}")
else:
    print("✅ Division successful!")
finally:
    print("🧩 This block always runs (cleanup or close files).")


# ==========================================================
# 3️⃣ Multiple Exception Handling Example
# ==========================================================
print("\n----- Multiple Exception Example -----")

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Division:", a / b)
except (ZeroDivisionError, ValueError):
    print("⚠️ Error: Invalid input or division by zero.")
else:
    print("✅ Operation successful!")
finally:
    print("✅ Program finished checking errors.")


# ==========================================================
# 4️⃣ Using Exception Object
# ==========================================================
print("\n----- Using Exception Object Example -----")

try:
    num = int(input("Enter a number: "))
    print(10 / num)
except Exception as e:
    print(f"Error Type: {type(e).__name__}")
    print(f"Error Details: {e}")


# ==========================================================
# 5️⃣ Raising Exceptions Manually
# ==========================================================
print("\n----- Raising Exception Manually -----")

def check_age(age):
    """Raises exception if age is less than 18."""
    if age < 18:
        raise ValueError("Age must be 18 or older to register.")
    else:
        print("✅ Access granted!")

try:
    age = int(input("Enter your age: "))
    check_age(age)
except ValueError as e:
    print(f"⚠️ Exception: {e}")


# ==========================================================
# 6️⃣ Try-Except Inside Functions
# ==========================================================
print("\n----- Try-Except Inside Function Example -----")

def divide_numbers(a, b):
    """Performs safe division using try-except."""
    try:
        return a / b
    except ZeroDivisionError:
        return "Division by zero is not allowed."
    except TypeError:
        return "Please enter valid numeric values."

num1 = input("Enter numerator: ")
num2 = input("Enter denominator: ")

try:
    num1 = float(num1)
    num2 = float(num2)
    print("Result:", divide_numbers(num1, num2))
except ValueError:
    print("⚠️ Invalid input: Please enter numeric values only.")


# ==========================================================
# 7️⃣ Nested Try-Except Example
# ==========================================================
print("\n----- Nested Try-Except Example -----")

try:
    num = int(input("Enter a number to divide 100: "))
    try:
        result = 100 / num
        print(f"Result = {result}")
    except ZeroDivisionError:
        print("⚠️ Cannot divide by zero inside nested block.")
except ValueError:
    print("⚠️ Invalid number entered.")
finally:
    print("✅ Nested try-except example complete.")


# ==========================================================
# 8️⃣ Using assert (for debugging)
# ==========================================================
print("\n----- Using assert Keyword Example -----")

try:
    age = int(input("Enter your age: "))
    assert age >= 18, "You must be 18 or older!"
    print("✅ Access granted.")
except AssertionError as e:
    print(f"⚠️ AssertionError: {e}")


# ==========================================================
# 9️⃣ Custom Exception Example
# ==========================================================
print("\n----- Custom Exception Example -----")

# Define your own exception class
class NegativeNumberError(Exception):
    """Custom exception for negative numbers."""
    pass

def check_positive(num):
    """Raises an exception if number is negative."""
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")
    else:
        print(f"✅ {num} is positive!")

try:
    num = int(input("Enter a positive number: "))
    check_positive(num)
except NegativeNumberError as e:
    print(f"⚠️ Custom Exception: {e}")
except ValueError:
    print("⚠️ Please enter a valid integer.")


# ==========================================================
# 🔟 Extra Example: Handling Multiple Built-in Exceptions
# ==========================================================
print("\n----- Handling Multiple Built-in Exceptions -----")

try:
    lst = [10, 20, 30]
    index = int(input("Enter list index to access: "))
    print(f"Value at index {index}: {lst[index]}")
except IndexError:
    print("⚠️ IndexError: Index out of range.")
except ValueError:
    print("⚠️ ValueError: Please enter a valid integer.")
except Exception as e:
    print(f"⚠️ Other Error: {type(e).__name__} → {e}")
else:
    print("✅ Successfully accessed element.")
finally:
    print("📘 End of multiple exception example.")


# ==========================================================
# 📘 Summary of Common Exceptions
# ==========================================================
"""
✅ Common Exception Types in Python:

0. IndentationError       → Improper indentation (spaces/tabs)
1. SyntaxError            → Missing punctuation, wrong syntax
2. ZeroDivisionError      → Divide by zero
3. ValueError             → Wrong data type (e.g., 'abc' to int)
4. TypeError              → Operation on wrong type (e.g., '2' + 2)
5. NameError              → Variable not defined
6. IndexError             → Index out of range in list
7. KeyError               → Missing key in dictionary
8. FileNotFoundError      → File does not exist
9. ImportError            → Cannot import module
10. AttributeError        → Attribute not found
11. AssertionError        → assert condition fails
"""

# ==========================================================
# ✅ End of error.py File
# ==========================================================
print("\n----- End of Error Handling Examples -----")
 