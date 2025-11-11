# ================================================
# Python - Bitwise Operators Explained
# ================================================

print("----- Bitwise Operators in Python -----")

# Bitwise operators are used to perform operations on binary numbers (bits: 0s and 1s).
# These operators work at the bit level (0 or 1).
# First, let’s see the binary form of numbers using the bin() function.

a = 10  # Binary: 1010
b = 4   # Binary: 0100

print("a =", a, "→", bin(a))
print("b =", b, "→", bin(b))


# ================================================
# Bitwise AND (&)
# ================================================
# Compares each bit of both numbers.
# Result bit = 1 only if both bits are 1.

print("\nBitwise AND (&):")
print("a & b =", a & b)         # 1010 & 0100 = 0000 0100 → 4
print("Binary:", bin(a & b))    # Output in binary


# ================================================
# Bitwise OR (|)
# ================================================
# Compares each bit of both numbers.
# Result bit = 1 if at least one bit is 1.

print("\nBitwise OR (|):")
print("a | b =", a | b)         # 1010 | 0100 = 1110 → 14
print("Binary:", bin(a | b))


# ================================================
# Bitwise XOR (^)
# ================================================
# XOR (Exclusive OR): Result bit = 1 if bits are different.

print("\nBitwise XOR (^):")
print("a ^ b =", a ^ b)         # 1010 ^ 0100 = 1110 → 14 - 8 = 6
print("Binary:", bin(a ^ b))


# ================================================
# Bitwise NOT (~)
# ================================================
# Inverts all bits.
# In Python, ~x = -(x + 1)

print("\nBitwise NOT (~):")
print("~a =", ~a)               # -(10 + 1) = -11
print("Binary:", bin(~a))


# ================================================
# Bitwise Left Shift (<<)
# ================================================
# Shifts bits to the left by a specified number of positions.
# Each shift left doubles the value.

print("\nBitwise LEFT SHIFT (<<):")
print("a << 1 =", a << 1)       # 1010 << 1 = 10100 → 20
print("a << 2 =", a << 2)       # 1010 << 2 = 101000 → 40
print("Binary:", bin(a << 2))


# ================================================
# Bitwise Right Shift (>>)
# ================================================
# Shifts bits to the right by a specified number of positions.
# Each shift right divides the value by 2.

print("\nBitwise RIGHT SHIFT (>>):")
print("a >> 1 =", a >> 1)       # 1010 >> 1 = 0101 → 5
print("a >> 2 =", a >> 2)       # 1010 >> 2 = 0010 → 2
print("Binary:", bin(a >> 2))


# ================================================
# Real-world Example
# ================================================
# Example: Checking if a number is even or odd using bitwise AND

print("\nCheck if number is even or odd:")
num = 7

if num & 1:  # If last bit is 1 → odd
    print(f"{num} is Odd")
else:
    print(f"{num} is Even")


# ================================================
# Summary Table
# ================================================
# Operator | Name            | Example | Result
# -----------------------------------------------
# &        | AND              | a & b   | 4
# |        | OR               | a | b   | 14
# ^        | XOR              | a ^ b   | 6
# ~        | NOT (Invert)     | ~a      | -11
# <<       | Left Shift       | a << 2  | 40
# >>       | Right Shift      | a >> 2  | 2

print("\n----- End of Bitwise Operators Example -----")
