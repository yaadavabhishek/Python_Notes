# ================================================
# Python - Escape Characters Explained
# ================================================

# Escape characters start with a backslash (\)
# They allow you to include special characters in strings
# Example: new lines, tabs, quotes, etc.

print("----- Escape Characters Examples -----")

# \n → New Line (moves text to the next line)
print("Hello\nWorld")   # Output:
# Hello
# World

# \t → Tab Space (adds horizontal spacing)
print("Name:\tAbhishek")   # Output: Name:    Abhishek

# \\ → Backslash (prints a single backslash)
print("This is a backslash: \\")  # Output: This is a backslash: \

# \" → Double Quote inside a double-quoted string
print("He said, \"Python is awesome!\"")  # Output: He said, "Python is awesome!"

# \' → Single Quote inside a single-quoted string
print('It\'s a beautiful day!')   # Output: It's a beautiful day!

# \b → Backspace (removes previous character)
print("Helloo\b")   # Output: Hello

# \r → Carriage Return (moves cursor to the beginning of the line)
print("Hello\rWorld")   # Output: World

# \f → Form Feed (used for page break, rarely used)
print("Hello\fWorld")   # Output: Hello
#                           World (depends on console)

# \ooo → Octal value (represents characters using octal code)
print("\110\145\154\154\157")   # Output: Hello

# \xhh → Hexadecimal value (represents characters using hex code)
print("\x48\x65\x6c\x6c\x6f")   # Output: Hello


# ================================================
# Raw Strings (r"string") → Ignore Escape Characters
# ================================================

# If you prefix a string with 'r', Python treats backslashes as plain text
print(r"Hello\nWorld")   # Output: Hello\nWorld
print(r"C:\Users\Abhishek")  # Output: C:\Users\Abhishek


# ================================================
# Real-world Use Example
# ================================================

# Example: file path
path = "C:\\Users\\Abhishek\\Desktop\\Python"
print(path)  # Output: C:\Users\Abhishek\Desktop\Python

# Example using raw string (simpler)
path2 = r"C:\Users\Abhishek\Desktop\Python"
print(path2)  # Output: C:\Users\Abhishek\Desktop\Python


# ================================================
# Summary Table (as comments)
# ================================================
# \n   → New Line
# \t   → Tab Space
# \\   → Backslash
# \"   → Double Quote
# \'   → Single Quote
# \b   → Backspace
# \r   → Carriage Return
# \f   → Form Feed
# \ooo → Octal value
# \xhh → Hexadecimal value
# r""  → Raw String (ignores escape sequences)

print("\n----- End of Escape Character Examples -----")
