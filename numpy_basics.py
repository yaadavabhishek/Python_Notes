# ============================================================
# 🧩 NumPy Deep Dive — Array Creation, Indexing & Operations
# ============================================================

# Install NumPy (if not installed)
# Command: pip install numpy
# --------------------------------

import numpy as np

# -------------------------------
# ✅ Creating a Python list
x = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
print("Python List:\n", x)

# -------------------------------
# ✅ Converting list to NumPy array
y = np.array(x)
print("\nNumPy Array:\n", y)

# ✅ Key Difference:
# - Python List: slower, flexible, allows mixed data types
# - NumPy Array: faster, fixed type, supports vectorized operations

# -------------------------------
# ✅ Creating arrays filled with zeros
zeros_array = np.zeros((3, 4))
print("\n3x4 Array of Zeros:\n", zeros_array)

# ✅ Creating array filled with a specific number
filled_with_neg5 = np.full((3, 4), -5)
print("\n3x4 Array Filled with -5:\n", filled_with_neg5)

# -------------------------------
# ✅ Arrays filled with ones
ones_array = np.ones((2, 3, 4), dtype=np.int16)
print("\n3D Array of Ones (2 blocks of 3x4):\n", ones_array)

# -------------------------------
# ✅ Identity matrix (useful in matrix algebra)
identity_matrix = np.eye(3)
print("\n3x3 Identity Matrix:\n", identity_matrix)

# -------------------------------
# ✅ Random arrays
random_array = np.random.random((2, 2))
print("\n2x2 Random Float Array (0.0 - 1.0):\n", random_array)

# -------------------------------
# ✅ Element-wise Operations (Automatic Broadcasting)
a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
b = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

print("\nArray A:\n", a)
print("Array B:\n", b)

print("\nElement-wise Addition (A + B):\n", a + b)
print("Element-wise Multiplication (A * B):\n", a * b)
print("Element-wise Subtraction (A - B):\n", a - b)
print("Element-wise Division (A / B):\n", a / b)

# -------------------------------
# ✅ Using np.arange()
arr = np.arange(0, 10, 1)
print("\nArray of integers from 0 to 9:\n", arr)

# Reshape to 2D (5 rows, 2 columns)
reshaped = arr.reshape(5, 2)
print("\nReshaped Array (5x2):\n", reshaped)

# -------------------------------
# ✅ Evenly spaced numbers with linspace()
linear_space = np.linspace(0, 1, 5)
print("\n5 Evenly Spaced Numbers from 0 to 1:\n", linear_space)

# -------------------------------
# ✅ Statistical Operations
print("\nMinimum value in 'a':", a.min())
print("Maximum value in 'a':", a.max())
print("Sum of all elements:", a.sum())
print("Mean (average):", a.mean())
print("Standard Deviation:", a.std())
print("Variance:", a.var())

# -------------------------------
# ✅ Random numbers
print("\nRandom 5 float numbers (0-1):", np.random.rand(5))
print("Random integer between 0 and 5:", np.random.randint(5))

# -------------------------------
# ✅ Index positions of min and max
print("\nIndex of Minimum in 'a':", a.argmin())
print("Index of Maximum in 'a':", a.argmax())

# -------------------------------
# ✅ Matrix Operations
print("\nMatrix Transpose of 'a':\n", a.T)
print("Matrix Multiplication (dot product):\n", np.dot(a, b))
print("Matrix Determinant:\n", np.linalg.det(a))
print("Inverse of 3x3 Identity Matrix:\n", np.linalg.inv(np.eye(3)))

# -------------------------------
# ✅ Array Metadata
print("\nShape of Array 'a':", a.shape)
print("Number of Dimensions:", a.ndim)
print("Data Type:", a.dtype)
print("Total Elements:", a.size)

# -------------------------------
# ✅ Flatten a 2D array → 1D
flat = a.flatten()
print("\nFlattened Array:\n", flat)

# ============================================================
# 🔍 INDEXING & SLICING
# ============================================================

x = np.arange(1, 21)
print("\n1D Array (1-20):\n", x)

print("9th element:", x[8])         # Index starts from 0
print("First 5 elements:", x[0:5])  # Slice 0–4
print("Last 5 elements:", x[-5:])   # Slice last 5
print("Elements from index 5 to end:", x[5:])
print("Every second element:", x[::2])
print("Every second element starting from index 1:", x[1::2])

# -------------------------------
# ✅ 2D Array Indexing
i_s = np.arange(25).reshape(5, 5)
print("\n2D Array (5x5):\n", i_s)

print("Element at row 5, column 3:", i_s[4, 2])
print("Element at row 2, column 3:", i_s[1, 2])
print("\nSub-array (rows 0-2, columns 1-3):\n", i_s[0:3, 1:4])

# -------------------------------
# ✅ Conditional Selection (Boolean Masking)
print("\nElements > 10:\n", i_s[i_s > 10])
print("Elements <= 10:\n", i_s[i_s <= 10])
print("Even numbers in array:\n", i_s[i_s % 2 == 0])

# ============================================================
# 🧮 NUMPY OPERATIONS
# ============================================================

num = np.arange(10)
num2 = np.arange(10, 20)

print("\nArray 1:", num)
print("Array 2:", num2)

# ✅ Universal Functions (ufuncs)
print("\nSine of each element:", np.sin(num))
print("Cosine of each element:", np.cos(num))
print("Square root of Array 2:", np.sqrt(num2))
print("Exponential of Array 1:", np.exp(num))
print("Logarithm of Array 2:", np.log(num2))
print("Power (Array1 ^ 2):", np.power(num, 2))

# -------------------------------
# ✅ Comparison Operations
print("\nnum > 5:", num > 5)
print("num == 5:", num == 5)
print("num != 5:", num != 5)

# -------------------------------
# ✅ Broadcasting Example
# Broadcasting allows NumPy to operate between arrays of different shapes
array1 = np.array([1, 2, 3])
array2 = np.array([[10], [20], [30]])
print("\nBroadcasting Example (array2 + array1):\n", array2 + array1)

# -------------------------------
# ✅ Aggregation Functions
matrix = np.arange(1, 10).reshape(3, 3)
print("\nMatrix:\n", matrix)
print("Row-wise sum:", matrix.sum(axis=1))
print("Column-wise sum:", matrix.sum(axis=0))
print("Row-wise mean:", matrix.mean(axis=1))
print("Column-wise max:", matrix.max(axis=0))

# -------------------------------
# ✅ Sorting & Unique Values
unsorted = np.array([10, 5, 8, 3, 5, 10, 2])
print("\nUnsorted Array:", unsorted)
print("Sorted Array:", np.sort(unsorted))
print("Unique Values:", np.unique(unsorted))
print("Indices of sorted order:", np.argsort(unsorted))

# -------------------------------
# ✅ Concatenation & Splitting
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print("\nConcatenate:", np.concatenate((arr1, arr2)))

# Splitting an array
split_example = np.arange(10)
print("Split into 2 parts:", np.array_split(split_example, 2))

# ============================================================
# 🧾 BONUS KNOWLEDGE
# ============================================================

# ✅ Save and Load Arrays
np.save("my_array.npy", num)
loaded = np.load("my_array.npy")
print("\nLoaded Array from File:", loaded)

# ✅ Reshape vs Resize
# reshape returns a new array, resize modifies in-place
reshaped = num.reshape(2, 5)
print("\nReshaped (2x5):\n", reshaped)

resized = np.resize(num, (3, 6))
print("\nResized (3x6):\n", resized)

# ✅ Copying Arrays
copy_array = num.copy()
print("\nCopied Array:", copy_array)

# ✅ Summary:
# NumPy is the foundation for:
# - Data Science (Pandas, Scikit-Learn)
# - Machine Learning (TensorFlow, PyTorch)
# - Image Processing (OpenCV)
# - Numerical Computation (SciPy)

print("\n✅ NumPy Operations Completed Successfully ✅")
