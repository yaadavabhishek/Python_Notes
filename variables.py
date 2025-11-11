# ==========================================
# 🧠 Python Variables - Complete Guide
# ==========================================

# ------------------------------------------
# 1️⃣ What is a Variable?
# ------------------------------------------
# A variable is a name given to a memory location that stores a value.
# You can think of it as a container for data.

name = "Abhishek"       # String variable
age = 25                 # Integer variable
height = 5.9             # Float variable
is_developer = True      # Boolean variable

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Developer?:", is_developer)

# ------------------------------------------
# 2️⃣ Variable Naming Rules
# ------------------------------------------
# ✅ Can contain letters, numbers, and underscores (_)
# ✅ Must start with a letter or underscore
# ❌ Cannot start with a number
# ❌ Cannot use special characters like @, $, %
# ✅ Case-sensitive (name, Name, NAME are all different)

# Examples:
my_name = "Abhi"
_name = "Private variable"
name123 = "Valid"
# 123name = "Invalid"  ❌
# my-name = "Invalid"  ❌
# class = "Invalid"    ❌ (reserved keyword)

# ------------------------------------------
# 3️⃣ Dynamic Typing
# ------------------------------------------
# Python is dynamically typed — you don't need to declare types.
x = 10
print("x is:", x)
x = "Now I am a string"
print("x changed to:", x)
x = [1, 2, 3]
print("x changed to a list:", x)

# ------------------------------------------
# 4️⃣ Multiple Assignment
# ------------------------------------------
# Assign multiple variables in one line
a, b, c = 10, 20, 30
print("a:", a, "b:", b, "c:", c)

# Assign same value to multiple variables
x = y = z = "Python"
print("x:", x, "y:", y, "z:", z)

# ------------------------------------------
# 5️⃣ Variable Types
# ------------------------------------------
# You can store different types of data in variables

name = "Abhishek"        # str
age = 25                 # int
height = 5.9             # float
is_active = True         # bool
skills = ["React", "Python", "Data Analysis"]   # list
person = {"name": "Abhishek", "age": 25}        # dict
data = (10, 20, 30)                            # tuple
nums = {1, 2, 3, 4, 5}                         # set
none_value = None                              # NoneType

print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of height:", type(height))
print("Type of is_active:", type(is_active))
print("Type of skills:", type(skills))
print("Type of person:", type(person))
print("Type of data:", type(data))
print("Type of nums:", type(nums))
print("Type of none_value:", type(none_value))

# ------------------------------------------
# 6️⃣ Variable Type Conversion
# ------------------------------------------
# Convert one data type to another (type casting)

x = 10
y = float(x)        # int to float
z = str(x)          # int to string
a = int(5.9)        # float to int

print("y (float):", y)
print("z (string):", z)
print("a (int):", a)

# ------------------------------------------
# 7️⃣ Constants (Convention)
# ------------------------------------------
# Python doesn't have real constants.
# By convention, we use ALL CAPS for constant-like variables.
PI = 3.14159
MAX_USERS = 100

print("PI:", PI)
print("MAX_USERS:", MAX_USERS)

# ------------------------------------------
# 8️⃣ Global vs Local Variables
# ------------------------------------------
# Variables declared inside a function are local by default.
# Variables declared outside are global.

global_var = "I am global"

def show_vars():
    local_var = "I am local"
    print(local_var)
    print(global_var)  # Can access global inside function

show_vars()
print(global_var)
# print(local_var)  ❌ Error: not defined outside function

# ------------------------------------------
# 9️⃣ Deleting Variables
# ------------------------------------------
x = 100
print("Before delete:", x)
del x               # Deletes variable from memory
# print(x)  ❌ Error: x is not defined

# ------------------------------------------
# 🔟 Useful Built-in Functions
# ------------------------------------------
a = 10
b = 20
print("id(a):", id(a))              # Unique memory address
print("type(a):", type(a))          # Data type
print("isinstance(a, int):", isinstance(a, int))  # Check type

# ------------------------------------------
# ✅ Summary
# ------------------------------------------
# - Variables store data in memory
# - No need to declare types (dynamic typing)
# - Follow naming rules (no special chars)
# - Multiple assignment possible
# - Use UPPERCASE for constants
# - Use type(), id(), isinstance() for info
