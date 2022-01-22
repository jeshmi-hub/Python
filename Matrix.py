from numpy import *

arr1 = array([

            [1,2,3],
            [4,5,6]

          ])

print(arr1.dtype)
print(arr1.ndim)
print(arr1.shape)
print(arr1.size)

arr2 = arr1.flatten()#flats the two dimensional array into one 
print(arr2)
