import numpy as np

arr = np.array([1, 2, 3])
print(type(arr))
print(arr)

# 0-D array - having only single element
rr = np.array(24)
print(rr)
# Check dimensions of the array
print(rr.ndim)

# 1-D array - having 0-D elements (multiple 0-D arrays)
arr = np.array([5, 6, 7, 8, 9])
print(arr)
# Check dimensions of the array
print(arr.ndim)


# 2d array containing two arrays with values 1,2,3 and 4,5,6
arrr = np.array([[1, 2, 3], [4, 5, 6]])
print(arrr)
# Check dimensions of the array
print(arrr.ndim)

# 3d array containing 2D arrays as its elements is called as the 3D array
arrrr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [11, 12, 32]]])
print(arrrr)
# Check dimensions of the array
print(arrrr.ndim)

# In this array the innermost dimension (5th) has 4 elements the 4th dimension
# has 1 element that is the vector , the 3d dim has 1 element that is
# the matrix with the vector , the 2d dim has 1 element that is the 3d
# array and 1st dim has 1 element that is 4d array

arr = np.array([1, 2, 3, 4], ndmin=1)
print(arr)
print("Number of dimensions is:", arr.ndim)

arr = np.array([1, 2, 3, 4], ndmin=2)
print(arr)
print("Number of dimensions is:", arr.ndim)

arr = np.array([1, 2, 3, 4], ndmin=3)
print(arr)
print("Number of dimensions is:", arr.ndim)

arr = np.array([1, 2, 3, 4], ndmin=4)
print(arr)
print("Number of dimensions is:", arr.ndim)

arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print("Number of dimensions is:", arr.ndim)

# change the data type any datatype like float,double
arr = np.array([1, 2, 3, 4], dtype=complex)
print(arr)
print('number of dimensions', arr.ndim)

# to check datatype of each
print('each item is of type', arr.dtype)

# checking datatype for 2d array with float datatype
arrr = np.array([[1, 2, 3], [4, 5, 6]], dtype='float')
print('array created by using list:\n', arrr)
print('each item is of type', arrr.dtype)

print('shape of array is', arrr.shape)
print('size of array', arrr.size)

# array indexing - used to access the array elements by referring to its index
# Indexes in numpy starts with 0
arr1 = ([1, 2, 3, 4])
print(arr1[0])

# for performing arithmetic operations
print(arr1[2] + arr1[3])
arrr = np.array([[1, 2, 3], [4, 5, 6]])

# array indexing - for 2d array
print('2nd element on first row', arrr[0, 1])
print('2nd element on second row', arrr[1, 1])
print('1st element on first row', arrr[0, 0])
print('1st element on second row', arrr[1, 0])

# Access the 3D arrays
arrrr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [11, 12, 32]]])
print(arrrr)
print(arrrr[0, 0, 0])
print(arrrr[0, 0, 1])
print(arrrr[0, 0, 2])
print(arrrr[0, 1, 0])
print(arrrr[1, 1, 1])

# Arange - Create the sequence of the integers using arange
arr = np.arange(11)
print(arr)
arrr = np.arange(12)
print(arrr)
arrr = np.arange(0, 20, 3)
print(arrr)

arrr = np.array([[1, 2, 3], [4, 5, 6]])
print(arrr.shape)
print(arrr[1, 1])
print(arrr[1, -1])