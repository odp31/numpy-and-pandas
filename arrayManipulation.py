# 1; reshaping arrays 

import numpy as np
arr = np.arange(12)
print(arr) # output; [0 1 2 3 4 5 6 7 8 9 10 11]

# reshape into 2d array
arr_reshaped = arr.reshape(3, 4)
print(arr_reshaped)

# 2; concatenating arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# concatenate horizontally 
arr_concat_h = np.concatenate((arr1, arr2))
print(arr_concat_h)

# concatenate vertically 
arr_concat_v = np.vstack((arr1, arr2))
print(arr_concat_v)

# 3; splitting arrays
arr = np.array([1, 2, 3, 4, 5, 6])
# split into two arrays
arr1, arr2 = np.split(arr, [3])
print(arr1)
print(arr2)


# 4; sorting arrays
arr = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
# sort array
arr_sorted = np.sort(arr)
print(arr_sorted)

# 5; filtering arrays
arr = np.array([1, 2, 3, 4, 5, 6])
# filter elements > 3 
filtered_arr = arr[arr>3]
print(filtered_arr)

#6; broadcasting
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([10, 20, 30])
# add b to each row of a
C = A + B
print(C)

# 7; advanced indexing
arr = np.arange(12).reshape(3, 4)
#select specific elements
print(arr[1:, 1:3]) # select rows 1 and 2, columns 1 and 2
