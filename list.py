# ================================================
# Python - List Explained
# ================================================

print("----- Python Lists -----")

# A list is a collection used to store multiple items in a single variable.
# Lists are ordered, changeable (mutable), and allow duplicate values.
# Lists are written with square brackets [].

# Creating a list
fruits = ["apple", "banana", "cherry", "mango"]
print("Fruits List:", fruits)

# ================================================
# Accessing List Items
# ================================================

print("\nAccessing Elements:")
print("First element:", fruits[0])     # apple
print("Second element:", fruits[1])    # banana
print("Last element:", fruits[-1])     # mango

# Slicing
print("Slicing (0:2):", fruits[0:2])   # ['apple', 'banana']


# ================================================
# Changing List Items
# ================================================

print("\nChanging Elements:")
fruits[1] = "orange"
print("After change:", fruits)         # ['apple', 'orange', 'cherry', 'mango']


# ================================================
# Adding Items
# ================================================

print("\nAdding Items:")

# append() → Adds item at the end
fruits.append("grapes")
print("After append:", fruits)

# insert() → Adds item at specific position
fruits.insert(1, "kiwi")
print("After insert:", fruits)

# extend() → Add elements from another list
tropical = ["papaya", "pineapple"]
fruits.extend(tropical)
print("After extend:", fruits)


# ================================================
# Removing Items
# ================================================

print("\nRemoving Items:")

# remove() → Removes specific item
fruits.remove("orange")
print("After remove:", fruits)

# pop() → Removes item at specific index (default: last)
fruits.pop()
print("After pop:", fruits)

# del → Delete by index
del fruits[0]
print("After del index 0:", fruits)

# clear() → Empties the list
# fruits.clear()
# print("After clear:", fruits)


# ================================================
# Looping Through a List
# ================================================

print("\nLooping through list:")
for fruit in fruits:
    print(fruit)


# ================================================
# List Comprehension
# ================================================
# Short way to create a new list based on existing one.

print("\nList Comprehension Example:")
numbers = [1, 2, 3, 4, 5, 6]
squared = [x ** 2 for x in numbers]
print("Original:", numbers)
print("Squared:", squared)


# ================================================
# Sorting Lists
# ================================================

print("\nSorting Lists:")

nums = [5, 2, 8, 1, 3]
nums.sort()  # Ascending
print("Ascending:", nums)

nums.sort(reverse=True)  # Descending
print("Descending:", nums)


# ================================================
# Copying a List
# ================================================

print("\nCopying Lists:")
new_list = fruits.copy()
print("Copied List:", new_list)


# ================================================
# Joining Two Lists
# ================================================

print("\nJoining Lists:")
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
joined = list1 + list2
print("Joined List:", joined)


# ================================================
# Built-in List Methods
# ================================================

print("\nCommon List Methods:")

sample = [10, 20, 30, 20, 10]

print("Length:", len(sample))
print("Count of 20:", sample.count(20))
print("Index of 30:", sample.index(30))
sample.reverse()
print("Reversed:", sample)


# ================================================
# Nested Lists (List within a List)
# ================================================

print("\nNested Lists:")
nested = [["a", "b", "c"], [1, 2, 3]]
print("Nested List:", nested)
print("Access inner item:", nested[1][2])  # Access '3' from second list


# ================================================
# Real-world Example
# ================================================

print("\nReal-world Example:")
shopping_cart = ["Milk", "Bread", "Eggs"]
print("Cart:", shopping_cart)

shopping_cart.append("Butter")
print("Added item:", shopping_cart)

if "Eggs" in shopping_cart:
    shopping_cart.remove("Eggs")
    print("Removed 'Eggs':", shopping_cart)


# ================================================
# Summary Table
# ================================================

# Method        | Description
# ------------------------------------------
# append()      | Adds element at end
# insert()      | Adds element at specific index
# remove()      | Removes specified element
# pop()         | Removes element by index
# clear()       | Removes all elements
# sort()        | Sorts list
# reverse()     | Reverses list
# copy()        | Copies list
# extend()      | Adds elements from another list
# count()       | Counts occurrences of value
# index()       | Finds index of value

print("\n----- End of List Example -----")
