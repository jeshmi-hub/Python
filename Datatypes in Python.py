a =  5.6
print(type(a))


b= int(a)
print(b)#coversion of float into int

print(int(True))#coversion of bool into int

li = [45,77,89]
print(type(li))

se = {57,8,89,90,66}
print(type(se))

t = (5,889,90,967)
print(type(t))

#range data type

o =range(0,10)
print(o)

print(list(o))#prints the list of numbers in the range

          
p = range(2,10,2)#2 starting point, 10 final point, 2 differnece between the numbers in range
print(list(p))

d = {'Jenny':'aMERICANO','Jeron': 'LAATTE','Sujin':'Tea'}
print(d.keys())
print(d.values())
print(d['Jenny'])
print(d.get('Sujin'))
