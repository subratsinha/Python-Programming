import numpy as np
num=[[1,2,3,4],[5,6,7,8],[10,11,15,17]]

arr=np.array(num)
arr=arr.astype('int32')
print("2darray :",arr)

print(arr.dtype)
print("1st row ",arr[0])
print("2nd row ",arr[1])
print("3rd row ",arr[2])


print("1st column:- ")
for col in arr:
    print(col[0],end=" ")
    

print("\n2nd column:- ")
for col in arr:
    print(col[1],end=" ")
    

print("\n3rd column:- ")
for col in arr:
    print(col[2],end=" ")
    
print("\n4th column:- ")
for col in arr:
    print(col[3],end=" ")
    
