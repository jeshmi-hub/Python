from array import *

arr = array('i',[])

n = int(input("Enter any value:"))

for i in range(n):
    x = int(input("Enter a value:"))
    arr.append(x)

print(arr)

val = int(input("Enter to search if the number is in array or not:"))

k=0

for e in arr:
    if e==val:
        print(k)
    k+=1
print(arr.index(val))
                
    
        


              

    
