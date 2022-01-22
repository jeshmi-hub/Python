from numpy import *

arr1 = array([

            [1,2,3,7,8,9],
            [4,5,6,10,2,43]

          ])

arr2 = arr1.flatten()

arr3 = arr2.reshape(3,4)#passing the rows and columns you want for the 3D array

arr4 = arr2.reshape(2,2,3)
print(arr3)
print(arr4)
