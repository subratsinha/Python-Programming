# to check whether an array contains any non zero element or not using numpy.


import numpy as np
lst1=[1,0,0,0,0]

arr1 = np.array(lst1)
print("Original array:")
print(arr1)
print("any ele. of  array is non-zero or not!:")
print(np.any(arr1))

lst2=[0,0,0,0,0]
arr2 = np.array(lst2)
print("Original array:")
print(arr2)
print("any ele. of  array is non-zero or not!:")
print(np.any(arr2))
