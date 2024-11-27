# fundamental library for scientific computing in python
# provides efficient array operations, linear algebra functions and random
# number generation capabilities 
import numpy as np
# 1. Creating Arrays
# one-dimensional array
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)

# two-dimensional array 
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)

# 2. Array Operations

# arithmetic
arr3 = arr1 + arr1
print(arr3)

# matrix multiplication
arr4 = np.dot(arr2, arr2.T)
print(arr4)

# element wise operations
arr5 = np.sqrt(arr1)
print(arr5)

# 3. Array Indexing and Slicing

# accessing elements
print(arr1[2]) # accessing third element

# slicing
print(arr1[1:4) # slicing from second to fourth element

# 4. Universal Functions 

# trigonmetric functions
arr6 = np.sin(arr1)
print(arr6)

# exponential functions 
arr7 = np.exp(arr1)
print(arr7)

# logarithmic functions
arr8 = np.log(arr1)
print(arr8)

# 5. Random Number Generation

# random integers 
random_integers = np.random.randint(1, 10, size=(3,3))
print(random_integers)

# random numbers from a normal distribution
random_normal = np.random.randn(5)
print(random_normal)

# 6. Linear Algebra

# solving linear equations
A = np.array([[1,2], [3,4]])
b = np.array([5,6)
x = np.linalg.solve(A,b)
print(x)

# calculating eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
print(eigenvalues)
print(eigenvectors)
