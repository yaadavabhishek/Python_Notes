# how install pandas
# pip install pandas
# check version

"""
===========================================================
 📘 Pandas Installation and Usage Guide
===========================================================

Pandas is a **Python library for data manipulation and analysis**.
It is widely used in **data analytics, data cleaning, data wrangling, 
and data visualization**.

It provides two main data structures:
- 🧾 Series → 1-dimensional labeled array (like a column in Excel)
- 📊 DataFrame → 2-dimensional labeled data (like an Excel sheet)

-----------------------------------------------------------
 STEP 1: Check if Python is Installed
-----------------------------------------------------------
Run in terminal:
    python --version
or
    python3 --version

If not installed, download it from:
https://www.python.org/downloads/

-----------------------------------------------------------
 STEP 2: Check if pip is Installed
-----------------------------------------------------------
Run in terminal:
    pip --version

If missing, install it:
    python -m ensurepip --upgrade

-----------------------------------------------------------
 STEP 3: Install Pandas
-----------------------------------------------------------
Run in terminal:
    pip install pandas

(For Python 3)
    pip3 install pandas

-----------------------------------------------------------
 STEP 4: Upgrade Pandas (Optional)
-----------------------------------------------------------
Run in terminal:
    pip install --upgrade pandas

-----------------------------------------------------------
 STEP 5: Verify Installation
-----------------------------------------------------------
Run in Python shell:
    import pandas as pd
    print(pd.__version__)

-----------------------------------------------------------
 OFFICIAL DOCUMENTATION:
-----------------------------------------------------------
📚 Visit: https://pandas.pydata.org/docs/

===========================================================
"""

# -----------------------------------------------------------
# ✅ Basic Usage of Pandas
# -----------------------------------------------------------

import pandas as pd

# -----------------------------
# Creating a Series (1D Data)
# -----------------------------
# A Series is like one column in a spreadsheet.
series_data = pd.Series([10, 20, 30, 40, 50], name="Numbers")
print("\n📘 Pandas Series:")
print(series_data)

# -----------------------------
# Creating a DataFrame (2D Data)
# -----------------------------
# A DataFrame is like a table with rows and columns.
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 28],
    "City": ["New York", "London", "Paris", "Tokyo"]
}
df = pd.DataFrame(data)
print("\n📊 Pandas DataFrame:")
print(df)

# -----------------------------
# Accessing Columns and Rows
# -----------------------------
print("\n🔹 Access Column 'Name':")
print(df["Name"])

print("\n🔹 Access Row using .loc:")
print(df.loc[1])   # Row with index 1

print("\n🔹 Access Row using .iloc:")
print(df.iloc[2])  # 3rd row (index-based)

# -----------------------------
# Basic Operations
# -----------------------------
print("\n🧮 Data Summary:")
print(df.describe())   # Statistics for numeric columns

print("\n📋 Data Info:")
print(df.info())       # Structure of the DataFrame

print("\n🔹 Shape of Data (rows, columns):", df.shape)

# -----------------------------
# Filtering Data
# -----------------------------
print("\n🔍 People aged over 28:")
print(df[df["Age"] > 28])

# -----------------------------
# Adding and Modifying Columns
# -----------------------------
df["Country"] = ["USA", "UK", "France", "Japan"]
df["Age in 5 Years"] = df["Age"] + 5
print("\n➕ After Adding Columns:")
print(df)

# -----------------------------
# Sorting Data
# -----------------------------
print("\n⬆️ Sort by Age:")
print(df.sort_values(by="Age", ascending=True))

# -----------------------------
# Handling Missing Values
# -----------------------------
print("\n⚠️ Handling Missing Data Example:")
data_with_nan = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Score": [85, None, 90, None]
}
df_nan = pd.DataFrame(data_with_nan)
print(df_nan)

# Fill missing values
print("\n✅ Fill Missing Values with 0:")
print(df_nan.fillna(0))

# Drop rows with missing data
print("\n❌ Drop Rows with Missing Values:")
print(df_nan.dropna())

# -----------------------------
# Reading & Writing Files
# -----------------------------
# (Make sure test.csv exists or create one with df.to_csv("test.csv"))
df.to_csv("sample_data.csv", index=False)
print("\n💾 Data saved to 'sample_data.csv'")

# Read back from CSV
loaded_df = pd.read_csv("sample_data.csv")
print("\n📂 Loaded Data from CSV:")
print(loaded_df)

# -----------------------------
# Version Check
# -----------------------------
print("\n🧩 Pandas Version:", pd.__version__)

"""
===========================================================
 💡 Quick Summary:
-----------------------------------------------------------
✅ Series → 1D labeled data (like Excel column)
✅ DataFrame → 2D labeled data (like Excel sheet)
✅ Operations: filter, sort, group, merge, reshape
✅ File Formats: CSV, Excel, JSON, SQL, etc.
✅ Common Methods: head(), tail(), describe(), info(), shape
===========================================================
"""
