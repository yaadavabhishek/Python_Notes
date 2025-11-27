# ==========================================
# 📘 module_test.py
# ==========================================
# Import your custom module (module.py must be in the same folder)
import module as calculator   # 'as calculator' gives it a short alias name

# Use functions from the module
result = calculator.add(10, 5)
print("Addition Result:", result)

print("Subtraction Result:", calculator.subtract(10, 3))

print("Multiplication Result:", calculator.multiply(10, 4))

print("Division Result:", calculator.divide(20, 4))

print("Power Result:", calculator.power(2, 5))

print("Square of 7:", calculator.square(7))

print("Modulus (10 % 3):", calculator.modulus(10, 3))

print("Floor Division (10 // 3):", calculator.floor_divide(10, 3))
