import numpy as np 

# 1; boolean indexing:
arr = np.array([1, 2, 3, 4, 5])
mask = arr > 3
filtered_arr = arr[mask]
print(filtered_arr) # output; [4 5]

# 2; fancing indexing:
arr = np.arange(12).reshape(3, 4)
indices = np.array([[0, 1], [2, 3]])
print(arr[indices])

# 3; broadcasting
# allows operations between arrays of different shapes 
# tries to braodcast smaller array to match shape of larger array 
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([10, 20, 30])
C = A + B
print(C)


# 4; universal functions (UFUNCS)
# functions that operate element-wise on arrays 
arr = np.array([1, 2, 3, 4, 5])
# element wise square root
sqrt_arr = np.sqrt(arr)
# element wise sine
sin_arr = np.sin(arr)

#5; linear algebra
# numpy.linalg provides functions for matrix operations, linear equations, etc
A = np.arary([[1, 2], [3, 4]])
B = np.array([5, 6], [7, 8]])

# matrix multiplication
C = np.dot(A, B)

# matrix inverse
inv_A = np.linalg.inv(A)


#6; random number generation
#generate random integers
random_integers = np.random.randint(1, 10, size=(3, 3))

# generate random floating point numbers
random_floats = np.random.rand(3, 3)

# generate random numbers from a normal distribution 
normal_dist = np.random.randn(100)
