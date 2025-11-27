# ==========================================================
# 📘 JSON Handling in Python
# ==========================================================
# The json module in Python is used to work with JSON data.
# JSON stands for JavaScript Object Notation.
# It is a lightweight data format for storing and sharing data.
# Commonly used for APIs, configuration files, and data exchange
# between web servers and clients.

import json

# ----------------------------------------------------------
# 1️⃣ Python Dictionary (Sample Data)
# ----------------------------------------------------------
data = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "is_student": False,
    "courses": ["Math", "Science", "Art"],
    "address": {
        "street": "123 Main St",
        "zip": "10001"
    },
    "skills": {
        "programming": ["Python", "JavaScript", "C++"],
        "tools": ["Git", "VS Code", "Jupyter Notebook"],
        "experience_years": 2
    },
    "grades": [85, 90, 88, 95],
    "active": True
}

# ----------------------------------------------------------
# 2️⃣ Convert Python Object to JSON String
# ----------------------------------------------------------
# json.dumps() → Converts Python data (dict, list, etc.) to JSON string.
# The indent=4 parameter makes the output more readable (pretty printing).

json_string = json.dumps(data, indent=4)
print("\n🟢 JSON Data (Converted from Python Dict):")
print(json_string)

# ----------------------------------------------------------
# 3️⃣ Save JSON Data to a File
# ----------------------------------------------------------
with open("student_data.json", "w") as file:
    json.dump(data, file, indent=4)
print("\n✅ Data successfully written to 'student_data.json'")

# ----------------------------------------------------------
# 4️⃣ Load JSON Data from a File (Deserialization)
# ----------------------------------------------------------
with open("student_data.json", "r") as file:
    loaded_data = json.load(file)

print("\n📘 Loaded Data from File:")
print(loaded_data)

# ----------------------------------------------------------
# 5️⃣ Accessing Data from JSON Object
# ----------------------------------------------------------
print("\n🎯 Accessing Individual Values:")
print("Name:", loaded_data["name"])
print("City:", loaded_data["city"])
print("First Course:", loaded_data["courses"][0])
print("Programming Skills:", loaded_data["skills"]["programming"])
print("Total Grades:", sum(loaded_data["grades"]))

# ----------------------------------------------------------
# 6️⃣ Convert JSON String Back to Python Dict
# ----------------------------------------------------------
# json.loads() → Converts JSON string into Python dictionary.
json_data = '{"company": "TechCorp", "employees": 120, "remote": true}'
python_dict = json.loads(json_data)

print("\n🔁 JSON String Converted to Python Dictionary:")
print(python_dict)

# ----------------------------------------------------------
# 7️⃣ Working with Complex Data
# ----------------------------------------------------------
# Example of nested structures (list + dict inside dict)
student_records = {
    "students": [
        {"id": 1, "name": "John", "marks": {"Math": 88, "Science": 92}},
        {"id": 2, "name": "Emma", "marks": {"Math": 75, "Science": 89}},
        {"id": 3, "name": "Liam", "marks": {"Math": 95, "Science": 94}},
    ]
}

# Save and reload this data
with open("students.json", "w") as file:
    json.dump(student_records, file, indent=4)

with open("students.json", "r") as file:
    data_back = json.load(file)

print("\n👩‍🎓 Student Records:")
for student in data_back["students"]:
    name = student["name"]
    avg = (student["marks"]["Math"] + student["marks"]["Science"]) / 2
    print(f"{name}'s average marks: {avg}")

# ----------------------------------------------------------
# 8️⃣ Sorting JSON keys alphabetically
# ----------------------------------------------------------
sorted_json = json.dumps(data, indent=4, sort_keys=True)
print("\n🔤 JSON with Sorted Keys:")
print(sorted_json)

# ----------------------------------------------------------
# 9️⃣ Handling Non-Serializable Objects (Example)
# ----------------------------------------------------------
# Some Python objects (like datetime) can’t be directly converted to JSON.
# You can use custom encoding using 'default' parameter.

from datetime import datetime

def custom_serializer(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()  # Convert datetime to string format
    raise TypeError("Type not serializable")

data_with_date = {
    "name": "Sophia",
    "joined_on": datetime.now()
}

json_with_date = json.dumps(data_with_date, indent=4, default=custom_serializer)
print("\n🕒 JSON with Date Serialized:")
print(json_with_date)

# ==========================================================
# END OF FILE
# ==========================================================
