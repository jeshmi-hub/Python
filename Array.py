from array import *

vals = array('i',[5,4,3,2,1])
vals.reverse()
print(vals)

for i in range(5):
    print(vals[i])

#new approach to execute numbers in array 
vals = array('i',[7,8,9,10])

newArr = array(vals.typecode,(a*a for a in vals))

for e in newArr:
    print(e)


#use of while loop
i = 0
while i<len(newArr):
    print(newArr[i])
    i+=1
