# ================================================
# Python Boolean Logic, Comparison & Conditional Statements
# ================================================

# -------- Comparison Operators --------
print('Comparison Operators:')
# Comparison operators compare two values and return a Boolean value: True or False

print(10 > 9)     # True, because 10 is greater than 9
print(10 == 9)    # False, because 10 is not equal to 9
print(10 < 9)     # False, because 10 is not less than 9


# -------- If-Else Conditional Statement --------
print('\nIf and else conditional statement:')
# Used to execute code based on a condition

a = 200
b = 33

if b > a:
    print("b is greater than a")  # This runs if the condition (b > a) is True
else:
    print("b is not greater than a")  # This runs if the condition is False


# -------- Evaluate String and Number with bool() --------
print('\nEvaluate a string and a number:')
# The bool() function evaluates a value and returns True or False

print(bool("Hello"))  # True → Non-empty string
print(bool(15))       # True → Non-zero number


# -------- Evaluate Two Variables --------
print('\nEvaluate two variables:')
x = "Hello"
y = 15

print(bool(x))  # True → Non-empty string
print(bool(y))  # True → Non-zero integer


# -------- Most Values are True --------
print('\nMost Values are True:')
# In Python, almost any value is considered True if it has some content.
# Exceptions: 0, empty string "", empty list [], empty dict {}, etc.

print(bool("abc"))                       # True → Non-empty string
print(bool(123))                         # True → Non-zero number
print(bool(["apple", "cherry", "banana"]))  # True → Non-empty list


# -------- Some Values are False --------
print('\nSome Values are False:')
# These values evaluate to False:
# False, None, 0, "", (), [], {}, etc.

print(bool(False))   # False
print(bool(None))    # False
print(bool(0))       # False
print(bool(""))      # False
print(bool(()))      # False
print(bool([]))      # False
print(bool({}))      # False


# -------- Custom Object with __len__() --------
print('\nCustom object with __len__ method:')
# If a class defines a __len__() method that returns 0, its object evaluates to False.

class MyClass:
    def __len__(self):
        return 0

myobj = MyClass()
print(bool(myobj))  # False → because __len__() returns 0


# -------- Function Returning a Boolean --------
print('\nPrint the answer of a function:')
# Functions can return Boolean values.

def myFunction():
    return True

print(myFunction())  # True


# -------- Execute Code Based on Boolean Function --------
print('\nExecute code based on Boolean answer:')
# Example: if the function returns True → print "YES!", else print "NO!"

def myFunction():
    return False  # You can change this to True to test the other outcome

if myFunction():
    print("YES!")   # Runs when myFunction() returns True
else:
    print("NO!")    # Runs when myFunction() returns False


# -------- Using isinstance() Function --------
print('\nUsing isinstance() function:')
# The isinstance() function checks whether an object is of a certain data type.

x = 200
print(isinstance(x, int))  # True → because x is an integer

# isinstance() can be used with any data type:
# isinstance(10.5, float) → True
# isinstance("Hello", str) → True
# isinstance([1, 2, 3], list) → True

