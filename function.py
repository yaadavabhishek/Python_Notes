# ================================================
# Python - Functions (User-Defined & Built-in)
# ================================================

from functools import reduce
print("----- Python Functions Explained -----")

# ================================================
# What is a Function?
# ================================================
# A function is a reusable block of code that performs a specific task.
# It helps make code modular, readable, and reusable.

# ================================================
# Defining a Function
# ================================================
# Syntax:
# def function_name(parameters):
#     "optional docstring"
#     function_body
#     return [expression]


def printme(str):
    """This function prints the string passed as an argument."""
    print(str)
    return


# ================================================
# Calling a Function
# ================================================
print("\n----- Calling a Function -----")
printme("This is the first call to the user-defined function!")
printme("Again, a second call to the same function!")

# ================================================
# Pass by Reference Example
# ================================================
print("\n----- Pass by Reference Example -----")


def changeme(mylist):
    """This changes a passed list within the function"""
    print("Values inside the function before change:", mylist)
    mylist[2] = 50
    print("Values inside the function after change:", mylist)
    return


mylist = [10, 20, 30]
changeme(mylist)
print("Values outside the function:", mylist)

# ================================================
# Function Arguments
# ================================================
# 1️⃣ Required Arguments
# 2️⃣ Keyword Arguments
# 3️⃣ Default Arguments
# 4️⃣ Variable-length Arguments (*args / **kwargs)

# ================================================
# Required Arguments
# ================================================
print("\n----- Required Arguments -----")


def greet(name):
    """This function greets the person with the given name"""
    print("Hello,", name)


greet("Abhishek")  # Must pass an argument, or it will cause an error

# ================================================
# Keyword Arguments
# ================================================
print("\n----- Keyword Arguments -----")


def printinfo(name, age):
    print("Name:", name)
    print("Age:", age)


printinfo(age=22, name="Abhishek")  # Order doesn’t matter when using keywords

# ================================================
# Default Arguments
# ================================================
print("\n----- Default Arguments -----")


def student(name, course="Python"):
    print("Name:", name)
    print("Course:", course)


student("Abhishek")
student("Yadav", "Data Science")

# ================================================
# Variable-Length Arguments
# ================================================
print("\n----- Variable-Length Arguments -----")

# Using *args for non-keyword variable arguments


def print_numbers(*numbers):
    print("Numbers passed:", numbers)
    for num in numbers:
        print(num)


print_numbers(10, 20, 30, 40)

# Using **kwargs for keyword variable arguments


def print_details(**details):
    print("Details:", details)
    for key, value in details.items():
        print(f"{key} → {value}")


print_details(name="Abhishek", age=22, city="Noida")

# ================================================
# Return Statement Example
# ================================================
print("\n----- Return Statement Example -----")


def add(a, b):
    """Returns the sum of two numbers"""
    return a + b


result = add(10, 20)
print("Sum:", result)

# ================================================
# The Anonymous (Lambda) Function
# ================================================
print("\n----- Lambda (Anonymous) Functions -----")

# Lambda syntax: lambda arguments: expression


def sum(arg1, arg2): return arg1 + arg2


print("Value of total:", sum(10, 20))
print("Value of total:", sum(20, 20))

# Example: Lambda with filter(), map(), reduce()
print("\nLambda with built-in functions:")

numbers = [1, 2, 3, 4, 5]

# Using map() to square numbers
squares = list(map(lambda x: x ** 2, numbers))
print("Squares:", squares)

# Using filter() to get even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", evens)

# Using reduce() to find product
product = reduce(lambda x, y: x * y, numbers)
print("Product of all numbers:", product)

# ================================================
# Docstring Example
# ================================================
print("\n----- Function Docstring Example -----")


def multiply(a, b):
    """This function multiplies two numbers and returns the result."""
    return a * b


print("Docstring:", multiply.__doc__)
print("Result:", multiply(5, 6))

# ================================================
# Nested Functions
# ================================================
print("\n----- Nested Functions Example -----")


def outer_function(text):
    def inner_function():
        print("Inner Function says:", text)
    inner_function()


outer_function("Hello from nested function!")

# ================================================
# Summary Table
# ================================================

# Function Type          | Description
# -----------------------------------------------------------
# Built-in Functions     | Already defined in Python (e.g., print(), len())
# User-defined Functions | Created using 'def' by the user
# Lambda Functions       | Anonymous one-line functions
# -----------------------------------------------------------
# Argument Types:
# Required Arguments     | Must be passed in correct order
# Keyword Arguments      | Passed by name
# Default Arguments      | Take default value if not passed
# Variable-Length Args   | Accept multiple values (*args, **kwargs)

print("\n----- End of Functions Example -----")

