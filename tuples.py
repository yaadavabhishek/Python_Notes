# ================================================
# Python - Tuple Explained
# ================================================

print("----- Python Tuples -----")

# A tuple is a collection used to store multiple items in a single variable.
# Tuples are ordered and immutable (cannot be changed).
# Tuples allow duplicate values and are written with parentheses ().

# Creating a Tuple
fruits = ("apple", "banana", "cherry", "mango")
print("Fruits Tuple:", fruits)


# ================================================
# Accessing Tuple Items
# ================================================

print("\nAccessing Elements:")
print("First element:", fruits[0])     # apple
print("Second element:", fruits[1])    # banana
print("Last element:", fruits[-1])     # mango

# Slicing
print("Slicing (1:3):", fruits[1:3])   # ('banana', 'cherry')


# ================================================
# Tuple Length
# ================================================

print("\nTuple Length:")
print("Length of fruits tuple:", len(fruits))


# ================================================
# Tuples are Immutable
# ================================================

print("\nTuples are Immutable:")
# fruits[1] = "orange"  # ❌ This will raise an error
print("You cannot modify tuples directly!")


# ================================================
# Creating Tuple with One Item
# ================================================

print("\nSingle Item Tuple:")
single_item = ("apple",)
print("Single-item tuple:", single_item)
print("Type:", type(single_item))

# Without comma, it will NOT be a tuple
not_tuple = ("apple")
print("Without comma:", not_tuple)
print("Type:", type(not_tuple))


# ================================================
# Looping Through a Tuple
# ================================================

print("\nLooping through Tuple:")
for fruit in fruits:
    print(fruit)


# ================================================
# Check if Item Exists
# ================================================

print("\nCheck if 'banana' in tuple:")
if "banana" in fruits:
    print("Yes, 'banana' is in the fruits tuple")


# ================================================
# Tuple Concatenation
# ================================================

print("\nTuple Concatenation:")
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
joined = tuple1 + tuple2
print("Joined Tuple:", joined)


# ================================================
# Repetition
# ================================================

print("\nTuple Repetition:")
numbers = (10, 20)
repeat = numbers * 3
print("Repeated Tuple:", repeat)


# ================================================
# Tuple Methods
# ================================================

print("\nTuple Methods:")
numbers = (1, 2, 3, 2, 4, 2)
print("Count of 2:", numbers.count(2))
print("Index of 3:", numbers.index(3))


# ================================================
# Converting Tuple to List (to modify)
# ================================================

print("\nConverting Tuple to List:")
x = ("apple", "banana", "cherry")
y = list(x)
y.append("orange")
x = tuple(y)
print("After modification:", x)


# ================================================
# Nested Tuples
# ================================================

print("\nNested Tuples:")
nested = (("a", "b", "c"), (1, 2, 3))
print("Nested Tuple:", nested)
print("Access inner element:", nested[1][2])  # Access 3


# ================================================
# Tuple Unpacking
# ================================================

print("\nTuple Unpacking:")
colors = ("red", "green", "blue")
(r, g, b) = colors
print("r:", r)
print("g:", g)
print("b:", b)

# Using Asterisk (*) for Unpacking
numbers = (1, 2, 3, 4, 5)
(a, b, *rest) = numbers
print("\nUnpacking with *:")
print("a:", a)
print("b:", b)
print("rest:", rest)


# ================================================
# Tuple Inside Loop Example
# ================================================

print("\nTuple Example with Loop:")
students = (("Abhi", 21), ("Riya", 22), ("Karan", 20))
for name, age in students:
    print(f"Name: {name}, Age: {age}")


# ================================================
# Summary Table
# ================================================

# Method        | Description
# ------------------------------------------
# count()       | Returns the number of times a value occurs
# index()       | Returns the index of the first occurrence
# + operator    | Concatenates tuples
# * operator    | Repeats tuple elements

print("\n----- End of Tuple Example -----")
