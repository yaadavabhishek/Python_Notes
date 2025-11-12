# ==========================================================
#  Python Loops – For, While, and Advanced Loop Concepts
# ==========================================================
# Loops allow you to execute a block of code repeatedly as long as a condition is true.
# Two main types: for loop, while loop

# ----------------------------------------------------------
# 🧮 1. Basic For Loop with List
# ----------------------------------------------------------
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Adding 5 to each number:")
for i in x:
    print(i + 5)
print()

# ----------------------------------------------------------
# 🎨 2. Loop Through a List of Strings
# ----------------------------------------------------------
colors = ['red', 'blue', 'green', 'yellow', 'black', 'white']
print("Colors in uppercase:")
for color in colors:
    print(color.upper())
print()

# ----------------------------------------------------------
# 🔢 3. Range in For Loop
# ----------------------------------------------------------
print("Squares of numbers from 1 to 10:")
for i in range(1, 11):
    print(f"{i}² = {i * i}")
print()

# ----------------------------------------------------------
# 🌀 4. Using range() without start argument
# ----------------------------------------------------------
for i in range(5):
    print("Iteration number:", i)
print()

# ----------------------------------------------------------
# 📥 5. User Input with Loops
# ----------------------------------------------------------
n = int(input("Enter a number: "))
for i in range(n):
    print("This is loop iteration:", i + 1)
print()

# ----------------------------------------------------------
# ⚠️ 6. While Loop
# ----------------------------------------------------------
count = 0
while count < 5:
    print("Count is:", count)
    count += 1  # Increment to avoid infinite loop
print("While loop finished!\n")

# ----------------------------------------------------------
# 🔠 7. Loop Through a String
# ----------------------------------------------------------
my_string = "Hello, World!"
print("Characters in string:")
for char in my_string:
    print(char)
print()

# ----------------------------------------------------------
# 🛑 8. Break Statement
# ----------------------------------------------------------
for i in range(10):
    if i == 5:
        print("Breaking loop at i =", i)
        break
    print("Current i:", i)
print()

# ----------------------------------------------------------
# ⏭️ 9. Continue Statement
# ----------------------------------------------------------
print("Printing only odd numbers using continue:")
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)
print()

# ----------------------------------------------------------
# 🔁 10. Nested Loops
# ----------------------------------------------------------
print("Nested loop example (pairs of i, j):")
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")
print()

# ----------------------------------------------------------
# ✅ 11. Loop with Else
# ----------------------------------------------------------
for i in range(3):
    print("Loop value:", i)
else:
    print("Loop completed successfully!")
print()

# ----------------------------------------------------------
# 🗝️ 12. Looping through a Dictionary
# ----------------------------------------------------------
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")
print()

# ----------------------------------------------------------
# 🧩 13. enumerate() Function
# ----------------------------------------------------------
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")
print()

# ----------------------------------------------------------
# 🔗 14. zip() Function
# ----------------------------------------------------------
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"Name: {name}, Age: {age}")
print()

# ----------------------------------------------------------
# 🧮 15. List, Dictionary, and Set Comprehensions
# ----------------------------------------------------------
squares = [x**2 for x in range(10)]
print("List comprehension:", squares)

squared_dict = {x: x**2 for x in range(5)}
print("Dictionary comprehension:", squared_dict)

squared_set = {x**2 for x in range(5)}
print("Set comprehension:", squared_set)
print()

# ----------------------------------------------------------
# ⚙️ 16. Generator Comprehension
# ----------------------------------------------------------
squared_gen = (x**2 for x in range(5))
print("Generator comprehension output:")
for num in squared_gen:
    print(num)
print()

# ----------------------------------------------------------
# 📁 17. Looping Through a File
# ----------------------------------------------------------
# Make sure a file named 'sample.txt' exists in the same folder.
# It will print each line without newlines.
with open('sample.txt', 'r') as file:
    for line in file:
        print(line.strip())
print()

# ----------------------------------------------------------
# 🧠 18. Advanced Looping with itertools
# ----------------------------------------------------------
import itertools

print("Combinations of ['A', 'B', 'C'] (2 at a time):")
for combination in itertools.combinations(['A', 'B', 'C'], 2):
    print(combination)

print("\nPermutations of ['A', 'B', 'C']:")
for permutation in itertools.permutations(['A', 'B', 'C']):
    print(permutation)

print("\nCartesian Product of ['A', 'B'] and [1, 2]:")
for product in itertools.product(['A', 'B'], [1, 2]):
    print(product)
print()

# ----------------------------------------------------------
# 🚀 19. Range with Step
# ----------------------------------------------------------
print("Even numbers from 0 to 20 using step=2:")
for i in range(0, 20, 2):
    print(i)
print()

# ----------------------------------------------------------
# 🔁 20. Reversing Loops
# ----------------------------------------------------------
print("Countdown from 10 to 1:")
for i in range(10, 0, -1):
    print(i)
print()

# Loop through list in reverse order
my_list = [1, 2, 3, 4, 5]
print("List in reverse order:")
for item in reversed(my_list):
    print(item)
print()

# ----------------------------------------------------------
# 🧮 21. Using map(), filter(), reduce()
# ----------------------------------------------------------
from functools import reduce

def square(x):
    return x ** 2

def is_even(x):
    return x % 2 == 0

def add(x, y):
    return x + y

numbers = [1, 2, 3, 4, 5]

print("Using map() to square numbers:")
squared_numbers = map(square, numbers)
for num in squared_numbers:
    print(num)

print("\nUsing filter() to get even numbers:")
even_numbers = filter(is_even, numbers)
for num in even_numbers:
    print(num)

print("\nUsing reduce() to sum numbers:")
sum_of_numbers = reduce(add, numbers)
print("Sum of numbers:", sum_of_numbers)
print()

# ----------------------------------------------------------
# 📊 22. Multiplication Table using Nested Loops
# ----------------------------------------------------------
print("Multiplication Table (1 to 10):")
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()
print()

# ----------------------------------------------------------
# 🔍 23. Find Prime Numbers using Loops
# ----------------------------------------------------------
def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("Prime numbers between 1 and 50:")
for num in range(1, 51):
    if is_prime(num):
        print(num)
print("\n----- End of Loops Examples -----")



#nested loop example
# Two lists containing adjectives and materials
x = ["big", "small", "bold", "light", "heavy"]
y = ["iron", "wood", "plastic", "glass", "stone"]

# Initialize counters
a = 0  # Index for list 'x'
b = 0  # Index for list 'y'

# Outer loop iterates through each item in 'x'
for i in x:
    # Inner loop iterates through each item in 'y'
    for j in y:
        # Print current combination of x[a] and y[b]
        print(x[a], y[b])
        
        # Move to the next index in list 'y'
        b += 1

    # After finishing one full inner loop, move to the next index in list 'x'
    a += 1

    # Reset 'b' to 0 so that we start from the first element of 'y' again
    b = 0

print("\n----- End of Nested Loop Example -----")

