#from array import *

#arr = array('i',[1,2,3,56,7])
#arr1 = array('i',[])

#for i in range(len(arr)):
    #arr1.append(arr[i]+5)
#print(arr1)
from numpy import *

arr1 = array([1,2,3,4,55])
arr2 = array([45,67,78,89,7])

arr3 = arr1 + arr2#vecotized operation

print(arr3)


print(sin(arr1))
print(sum(arr2))
print(sort(arr3))
print(concatenate([arr1,arr2]))

