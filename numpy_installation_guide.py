# how install numpy
# pip install numpy 
# check version

"""
===========================================================
 NumPy Installation and Usage Guide
===========================================================

NumPy (Numerical Python) is a library for numerical and scientific computing.
It provides tools for:
- Working with multi-dimensional arrays
- Mathematical, logical, and statistical operations
- Linear algebra, Fourier transforms, and random numbers

-----------------------------------------------------------
 STEP 1: Check if Python is Installed
-----------------------------------------------------------
Run in terminal:
    python --version
or
    python3 --version

If Python isn’t installed, download it from:
https://www.python.org/downloads/

-----------------------------------------------------------
 STEP 2: Check if pip is Installed
-----------------------------------------------------------
Run in terminal:
    pip --version

If pip is missing, install it:
    python -m ensurepip --upgrade

-----------------------------------------------------------
 STEP 3: Install NumPy
-----------------------------------------------------------
Run in terminal:
    pip install numpy
or (for Python 3)
    pip3 install numpy

-----------------------------------------------------------
 STEP 4: Upgrade NumPy (Optional)
-----------------------------------------------------------
Run in terminal:
    pip install --upgrade numpy

-----------------------------------------------------------
 STEP 5: Verify Installation
-----------------------------------------------------------
Run in Python shell:
    import numpy as np
    print(np.__version__)

-----------------------------------------------------------
 OFFICIAL DOCUMENTATION:
-----------------------------------------------------------
Visit: https://numpy.org/doc/
===========================================================
"""

import numpy as np

# Creating a 1D array
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr1)

# Creating a 2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", arr2)

# Performing mathematical operations
print("Sum of elements:", np.sum(arr1))
print("Mean value:", np.mean(arr1))
print("Max value:", np.max(arr1))
print("Square roots:", np.sqrt(arr1))

# Working with random numbers
random_arr = np.random.randint(1, 50, size=(3, 3))
print("Random Array:\n", random_arr)

# Checking version
print("NumPy Version:", np.__version__)
