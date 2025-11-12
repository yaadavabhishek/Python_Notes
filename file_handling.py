# ==========================================
# 📂 Python File Handling Example
# ==========================================
# Modes in file handling:
# 'r' → Read (file must exist)
# 'w' → Write (creates new file / overwrites existing)
# 'a' → Append (adds new data at the end of file)
# 'x' → Create (fails if file exists)
# 'b' → Binary mode (used for images, videos, etc.)
# 't' → Text mode (default)

# ==========================================
# 1️⃣ Reading from a file
# ==========================================
# Open file in read mode ('r')
file = open('test_file.txt', 'r')

# Read entire file content into a single string
content = file.read()

print("📖 File Content:")
print(content)

# Close the file after reading (good practice)
file.close()


# ==========================================
# 2️⃣ Writing (Appending) to a file
# ==========================================
# Open file in append mode ('a')
# Note: 'a' mode will *not erase* existing content, it adds at the end
file = open('test_file.txt', 'a')

# Create a dictionary (sample data)
person = {"name": "John", "age": 30, "city": "New York"}

# Convert dictionary to string using str() and write it to the file
file.write("Person Data: " + str(person) + "\n")

# Close the file after writing
file.close()


# ==========================================
# 3️⃣ Appending multiple lines at once
# ==========================================
lines_to_append = [
    "Hello, World!\n",
    "This is a test file.\n",
    "Python file handling is easy!\n"
]

# Using 'with open' automatically closes the file after the block
with open('test_file.txt', 'a') as file:
    file.writelines(lines_to_append)  # Append multiple lines at once


# ==========================================
# 4️⃣ Reading the updated file
# ==========================================
# Using 'with' again for safe and cleaner file handling
with open('test_file.txt', 'r') as file:
    updated_content = file.read()
    print("🆕 Updated File Content:")
    print(updated_content)


# ==========================================
# 🧠 Extra Knowledge Section
# ==========================================

# 1️⃣ Reading file line by line
# with open('test_file.txt', 'r') as file:
#     for line in file:
#         print(line.strip())  # .strip() removes newline characters

# 2️⃣ Writing a NEW file (overwriting if exists)
# with open('new_file.txt', 'w') as file:
#     file.write("This file is newly created!\n")

# 3️⃣ Using 'x' mode to create file safely (throws error if already exists)
# try:
#     with open('safe_create.txt', 'x') as file:
#         file.write("New file created successfully!")
# except FileExistsError:
#     print("⚠️ File already exists!")

# 4️⃣ Checking if file exists before reading
import os
if os.path.exists('test_file.txt'):
    print("✅ File exists and ready to use.")
else:
    print("❌ File not found.")

# 5️⃣ Deleting a file safely (optional)
# if os.path.exists('unwanted_file.txt'):
#     os.remove('unwanted_file.txt')
#     print("🗑️ File deleted successfully.")
# else:
#     print("⚠️ File does not exist, cannot delete.")
