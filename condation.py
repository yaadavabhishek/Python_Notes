# ==========================================================
#  Python Conditional Statements (if, elif, else)
# ==========================================================
# Conditional statements are used to make decisions in a program.
# They execute different blocks of code based on whether a condition is True or False.

# ----------------------------------------------------------
# 🧩 Basic if-else Example
# ----------------------------------------------------------
x = 10
y = 10

if x == y:
    print("✅ x is equal to y")
else:
    print("❌ x is not equal to y")

print("Program is working fine\n")


# ----------------------------------------------------------
# 🧮 if-elif-else Example
# ----------------------------------------------------------
a = 10
b = 20
c = 30

# Only one block executes — whichever condition is True first.
if a == b:
    print("a is equal to b")
elif b == c:
    print("b is equal to c")
else:
    print("Neither a equals b nor b equals c")

print()  # Empty line for readability


# ----------------------------------------------------------
# 🔤 String Comparison Example
# ----------------------------------------------------------
greeting = "Hello"

if greeting == "Hello":
    print("👋 Greeting detected")
else:
    print("No greeting detected")

print()


# ----------------------------------------------------------
# ⚙️ Multiple Conditions using Logical Operators
# ----------------------------------------------------------
num1 = 15
num2 = 25
num3 = 35

# AND → All conditions must be True
if (num1 < num2) and (num2 < num3):
    print("✅ num1 < num2 and num2 < num3 (Both True)")
else:
    print("❌ Condition not met")

# OR → At least one condition must be True
if (num1 < num2) or (num2 > num3):
    print("✅ At least one condition is True")
else:
    print("❌ Both conditions are False")

# NOT → Reverses the result
if not (num1 > num2):
    print("✅ num1 is NOT greater than num2")
else:
    print("❌ num1 is greater than num2")

print()


# ----------------------------------------------------------
# 🔁 Combining if, elif, else
# ----------------------------------------------------------
x = 10
y = 20

if x == y:
    print("x is equal to y")
elif x != y:
    print("x is NOT equal to y")
else:
    print("No matching condition found")

print()


# ----------------------------------------------------------
# 🧠 Nested if Example (if inside another if)
# ----------------------------------------------------------
num = int(input("Enter a number: "))

if num > 0:
    if num % 2 == 0:
        print("✅ Positive even number")
    else:
        print("✅ Positive odd number")
else:
    print("❌ Non-positive number")

print()


# ----------------------------------------------------------
# ✅ Real-world Example: Check Eligibility
# ----------------------------------------------------------
age = int(input("Enter your age: "))

if age >= 18:
    if age >= 60:
        print("You are a senior citizen.")
    else:
        print("You are an adult.")
else:
    print("You are a minor.")

print()


# ----------------------------------------------------------
# 🧾 Grading System Example
# ----------------------------------------------------------
score = int(input("Enter your score (0-100): "))

if score >= 90:
    print("🎯 Grade: A (Excellent)")
elif score >= 75:
    print("👍 Grade: B (Good)")
elif score >= 50:
    print("🙂 Grade: C (Average)")
else:
    print("⚠️ Grade: F (Fail)")

print()


# ----------------------------------------------------------
# 🔍 Using assert for Custom Condition Checking
# ----------------------------------------------------------
print("\n----- Custom Assertion Example -----")

def validate_score(score):
    """Validates that the score is between 0 and 100."""
    # If the condition fails, AssertionError is raised
    assert 0 <= score <= 100, "⚠️ Score must be between 0 and 100"
    print("✅ Valid score:", score)

try:
    score = int(input("Enter a score to validate (0-100): "))
    validate_score(score)
except AssertionError as e:
    print(e)

print("\n----- End of Conditional Statements Example -----")
