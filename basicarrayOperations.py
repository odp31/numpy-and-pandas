import numpy as np

# create a 1D array
arr1 = np.array([1, 2, 3, 4, 5])

# create 2d array
arr2 = np.array([1, 2, 3], [4, 5, 6]])

# array operations
print(arr1 + 2) # add 2 to each element
print(arr1 * 2)   # multiple each element by 2
print(arr1 * arr2) # element wise multiplication
print(np.dot(arr1, arr2.T)) # dot product 
