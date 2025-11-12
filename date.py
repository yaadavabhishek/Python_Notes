# -------------------------------
# 📅 Python DateTime Module Example
# -------------------------------

import datetime   # Import the built-in datetime module

# Get the current date and time from the system clock
now = datetime.datetime.now()   
print("Current date and time:", now)

# -------------------------------
# 🔹 Extracting individual components
# -------------------------------
print(now.year)          # Current year (e.g., 2025)
print(now.month)         # Current month (1–12)
print(now.day)           # Current day of the month (1–31)
print(now.hour)          # Current hour (0–23)
print(now.minute)        # Current minute (0–59)
print(now.second)        # Current second (0–59)
print(now.microsecond)   # Current microsecond (0–999999)

# -------------------------------
# 🔹 Day of the week
# -------------------------------
print(now.weekday())     # Returns integer (0=Monday, 6=Sunday)
print(now.isoweekday())  # Returns integer (1=Monday, 7=Sunday)

# -------------------------------
# 🔹 Other datetime representations
# -------------------------------
print(now.timetuple())   # Returns a struct_time tuple (used for time-related functions)
print(now.isoformat())   # ISO 8601 format string (e.g., "2025-11-12T10:30:45.123456")

# -------------------------------
# 🔹 Formatting datetime as a custom string
# -------------------------------
# strftime() = string format time → convert datetime to readable string
print(now.strftime("%Y-%m-%d %H:%M:%S"))  
# Example output: 2025-11-12 10:30:45

# Common formatting codes:
# %Y → Year (e.g. 2025)
# %m → Month (01–12)
# %d → Day (01–31)
# %H → Hour (00–23)
# %M → Minute (00–59)
# %S → Second (00–59)
# %A → Full weekday name (e.g., Wednesday)
# %B → Full month name (e.g., November)
# %I → Hour (01–12, for 12-hour clock)
# %p → AM or PM

# -------------------------------
# 🔹 Creating a specific date and time manually
# -------------------------------
specific_date = datetime.datetime(2020, 5, 17, 15, 30, 45)
# Year=2020, Month=May(5), Day=17, Time=15:30:45
print("Specific date and time:", specific_date)

# -------------------------------
# 🔹 Format the specific date in a human-friendly style
# -------------------------------
formatted_date = specific_date.strftime("%A, %B %d, %Y at %I:%M %p")
# Example output: Sunday, May 17, 2020 at 03:30 PM
print("Formatted specific date:", formatted_date)

# -------------------------------
# 🧠 Extra Knowledge Section
# -------------------------------

# 1️⃣ Get only the current date (without time)
today = datetime.date.today()
print("Today's date:", today)

# 2️⃣ Get only the current time (without date)
current_time = datetime.datetime.now().time()
print("Current time:", current_time)

# 3️⃣ Add or subtract days using timedelta
from datetime import timedelta
future_date = now + timedelta(days=7)     # Add 7 days
past_date = now - timedelta(days=30)      # Subtract 30 days
print("Date after 7 days:", future_date)
print("Date 30 days ago:", past_date)

# 4️⃣ Convert string to datetime (reverse of strftime → strptime)
date_str = "2025-11-12 14:45:30"
converted_date = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print("Converted from string:", converted_date)

# 5️⃣ Get UTC time (Coordinated Universal Time)
utc_now = datetime.datetime.utcnow()
print("Current UTC time:", utc_now)

