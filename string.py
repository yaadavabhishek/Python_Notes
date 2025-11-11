# Define a string variable
name = 'Abhishek Yadav'

# Print the full string
print(name)  # Output: Abhishek Yadav

# Slice the string from index 0 to 6 (7 excluded)
print(name[0:7])  # Output: Abhishe

# Find the index (position) of the first occurrence of 'Y'
print(name.index('Y'))  # Output: 9

# Count how many times 'a' appears in the string (case-sensitive)
print(name.count('a'))  # Output: 1 (since 'A' is uppercase, only small 'a' is counted)

# Check if string starts with 'A'
print(name.startswith('A'))  # Output: True

# Check if string ends with 'd'
print(name.endswith('d'))  # Output: True

# Capitalize only the first character of the string and make others lowercase
print(name.capitalize())  # Output: Abhishek yadav

# Convert the first letter of each word to uppercase
print(name.title())  # Output: Abhishek Yadav

# Check if all characters are alphabetic (no spaces allowed)
print(name.isalpha())  # Output: False (because there is a space)

# Find index of first occurrence of 'h'
print(name.find('h'))  # Output: 3

# Center align the string in 50-character width, filling empty space with '*'
print(name.center(50, '*'))

# Swap uppercase to lowercase and vice versa
print(name.swapcase())  # Output: aBHISHEK yADAV

# Right justify the string to width 50 (spaces added to the left)
print(name.rjust(50))

# Left justify the string to width 50, fill remaining space with '-'
print(name.ljust(50, '-'))

# Remove 'd' characters from the start and end (not from middle)
print(name.strip('d'))  # Output: Abhishek Yava

# Encode string into bytes using default 'utf-8'
print(name.encode())  # Output: b'Abhishek Yadav'

# Return a formatted version (here no placeholders used)
print(name.format())  # Output: Abhishek Yadav

# Check if all characters are lowercase
print(name.islower())  # Output: False

# Check if all characters are uppercase
print(name.isupper())  # Output: False

# Split string into 3 parts around first space: (before, separator, after)
print(name.partition(' '))  # Output: ('Abhishek', ' ', 'Yadav')

# Pad string with zeros on the left to make total length 30
print(name.zfill(30))

# Replace all 'A' with 'a' using translation table
print(name.translate(str.maketrans('A', 'a')))

# Expand tab characters '\t' to spaces (not visible since no tabs here)
print(name.expandtabs())

# Remove a specific prefix (if present)
print(name.removeprefix('Abhi'))  # Output: shek Yadav

# Remove a specific suffix (if present)
print(name.removesuffix('Yadav'))  # Output: Abhishek

# Return lowercase version suitable for case-insensitive comparisons
print(name.casefold())  # Output: abhishek yadav

# Split string at line breaks (\n)
print(name.splitlines())  # Output: ['Abhishek Yadav']

# Check if all characters are printable (no control chars)
print(name.isprintable())  # Output: True

# Check if valid Python identifier (no spaces or digits allowed)
print(name.isidentifier())  # Output: False

# Check if string contains only numeric characters
print(name.isnumeric())  # Output: False

# Check if string contains only decimal digits
print(name.isdecimal())  # Output: False

# Check if string contains only digits (includes unicode digits)
print(name.isdigit())  # Output: False

# Join elements of a list with 'name' string in between
print(name.join(['Hello', 'World']))  # Output: HelloAbhishek YadavWorld

# Split string into 3 parts around the last space
print(name.rpartition(' '))  # Output: ('Abhishek', ' ', 'Yadav')

# Encode string to bytes using UTF-8
print(name.encode('utf-8'))  # Output: b'Abhishek Yadav'

# Encode using ASCII and ignore non-ASCII characters (none here)
print(name.encode('ascii', 'ignore'))  # Output: b'Abhishek Yadav'

# Use magic method to concatenate another string
print(name.__add__(' is a Data Analyst'))  # Output: Abhishek Yadav is a Data Analyst

# Return length of string
print(name.__len__())  # Output: 14

# Check if substring 'Yadav' exists
print(name.__contains__('Yadav'))  # Output: True

# Get character by index using magic method
print(name.__getitem__(0))  # Output: A

# Return the string itself (string representation)
print(name.__str__())  # Output: Abhishek Yadav

# Return a developer-friendly string representation
print(name.__repr__())  # Output: 'Abhishek Yadav'

# Return all available attributes and methods of string object
print(name.__dir__())

# Custom formatted string with width 50 and center aligned (^)
print(name.__format__('^50'))

# Return hash value of the string (used in dictionaries/sets)
print(name.__hash__())

# Return memory size of the string object in bytes
print(name.__sizeof__())

# Return the class type of the object
print(name.__class__)  # Output: <class 'str'>

# Return the documentation string for str class
print(name.__doc__)  # Output: Built-in immutable sequence of Unicode characters.

# Compare equality with another string
print(name.__eq__('Abhishek Yadav'))  # Output: True

# Compare inequality with another string
print(name.__ne__('Abhishek Yadav'))  # Output: False

# Lexicographical comparison (less than)
print(name.__lt__('Zehishek Yadav'))  # Output: True

# ----- End of String Methods Section -----

# Slice a substring from index 2 to 9
print(name[2:10])  # Output: hishek Y

# Get total number of characters in string
print(len(name))  # Output: 14

# Convert string to lowercase
print(name.lower())  # Output: abhishek yadav

# Convert string to uppercase
print(name.upper())  # Output: ABHISHEK YADAV

# Replace all occurrences of 'A' with 'a'
print(name.replace('A', 'a'))  # Output: abhishek Yadav

# Split string into a list of words
print(name.split())  # Output: ['Abhishek', 'Yadav']

# String concatenation using '+'
first_name = 'Abhishek'
last_name = 'Yadav'
full_name = first_name + ' ' + last_name
print(full_name)  # Output: Abhishek Yadav

# ---- F-Strings ----
# Introduced in Python 3.6, f-strings allow variable substitution inside strings.
new_first_name = 'Abhishek'
new_last_name = 'Yadav'
new_full_name = f'{new_first_name} {new_last_name}'
print(new_full_name)  # Output: Abhishek Yadav

# =======================================================================================================================================

# ==========================================
# 🧠 Most Commonly Used String Methods in Python
# ==========================================

name = "Abhishek Yadav"
print("Original String:", name)

# ------------------------------------------
# 1️⃣ Basic Info
# ------------------------------------------
print("Length of string:", len(name))               # Total number of characters
print("Type of variable:", type(name))              # Shows data type

# ------------------------------------------
# 2️⃣ Accessing and Slicing
# ------------------------------------------
print("First character:", name[0])                  # Access a single character
print("First 5 characters:", name[0:5])             # Slice part of the string

# ------------------------------------------
# 3️⃣ Searching
# ------------------------------------------
print("Find 'Y':", name.find('Y'))                  # Index of first occurrence or -1
print("Index of 'Y':", name.index('Y'))             # Index (throws error if not found)
print("Count of 'a':", name.count('a'))             # Count occurrences
print("Starts with 'A'?:", name.startswith('A'))    # Check if starts with 'A'
print("Ends with 'd'?:", name.endswith('d'))        # Check if ends with 'd'

# ------------------------------------------
# 4️⃣ Case Conversion
# ------------------------------------------
print("Uppercase:", name.upper())                   # Convert to UPPERCASE
print("Lowercase:", name.lower())                   # Convert to lowercase
print("Capitalize:", name.capitalize())             # First letter capitalized
print("Title Case:", name.title())                  # Every word capitalized
print("Swap Case:", name.swapcase())                # Swap lower/upper

# ------------------------------------------
# 5️⃣ Trimming and Cleaning
# ------------------------------------------
text = "   hello world   "
print("Original with spaces:", repr(text))
print("strip():", text.strip())                     # Remove both-side spaces
print("lstrip():", text.lstrip())                   # Remove left spaces
print("rstrip():", text.rstrip())                   # Remove right spaces

# ------------------------------------------
# 6️⃣ Replace and Split
# ------------------------------------------
sentence = "I love Python programming"
print("Replace 'Python' with 'Java':", sentence.replace('Python', 'Java'))   # Replace text
print("Split by space:", sentence.split())           # Split into list by space
print("Split by 'o':", sentence.split('o'))          # Split by custom character
print("Join list with '-':", "-".join(['a', 'b', 'c'])) # Join list into a string

# ------------------------------------------
# 7️⃣ Validation & Checking
# ------------------------------------------
word = "Python3"
print("Is alpha?:", word.isalpha())                 # Only letters?
print("Is digit?:", word.isdigit())                 # Only digits?
print("Is alphanumeric?:", word.isalnum())          # Letters or digits?
print("Is space?:", "   ".isspace())                # Only spaces?
print("Is lower?:", word.islower())                 # All lowercase?
print("Is upper?:", word.isupper())                 # All uppercase?
print("Is title?:", word.istitle())                 # Title case?

# ------------------------------------------
# 8️⃣ Formatting
# ------------------------------------------
first_name = "Abhishek"
last_name = "Yadav"

# Using + operator (concatenation)
full_name = first_name + " " + last_name
print("Using + :", full_name)

# Using format()
formatted = "My name is {} {}".format(first_name, last_name)
print("Using format():", formatted)

# Using f-string (recommended)
f_string = f"My name is {first_name} {last_name}"
print("Using f-string:", f_string)

# Using % formatting (older style)
percent_style = "My name is %s %s" % (first_name, last_name)
print("Using % formatting:", percent_style)

# ------------------------------------------
# 9️⃣ Useful Extras
# ------------------------------------------
print("Replace example:", name.replace("Abhi", "Abhii"))
print("Split example:", name.split())
print("Join example:", " ".join(["Hello", "World"]))
print("Check substring:", "Yadav" in name)          # True if substring exists
print("Convert to bytes:", name.encode())           # Encode to bytes
print("Center text:", name.center(40, '*'))         # Center align with *

# ------------------------------------------
# ✅ Summary
# ------------------------------------------
# len()       → Length of string
# find()      → Search substring (returns index or -1)
# count()     → Count occurrences
# startswith(), endswith() → Prefix/suffix check
# upper(), lower(), title(), swapcase() → Case conversion
# strip(), lstrip(), rstrip() → Remove whitespace
# replace(), split(), join() → Modify or merge strings
# isalpha(), isdigit(), isalnum() → Validation
# format(), f-string → String formatting
# encode(), center() → Encoding and alignment
# These methods form the backbone of string manipulation in Python and are widely used in data processing, web development, and more.


