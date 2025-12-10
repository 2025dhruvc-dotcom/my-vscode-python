import numpy as np
arr = np.array([1, 2, 3, 4])

print("Data type of the array elements:", arr.dtype)



arr = np.array([1.5, 2.5, 3.5, 4.5])
print("Data type of the array elements:", arr.dtype)


arr = np.array(['apple', 'banana', 'cherry'])
print("Data type of the array elements:", arr.dtype)

arr = np.array([1, 2, 3, 4], dtype=np.float64)
print("Data type of the array elements after specifying dtype:", arr.dtype)