def add_sub(x,y):
    c = x + y
    d = x - y
    return c,d

result1,result2 = add_sub(5,4)
print(result1,result2)

def sum(a,*b):#use of * lets us pass store or pass multiple values in a variable
    c = a

    for i in b:
        c = c + i
    print(c)

sum(5,6,34,78)


#keyworded variables argument

def person(name, **data):
    print(name)

    for i,j in data.items():#items function is used to fetch the values stored in the argument data
        print(i,j)

person('jeshmi',age= 20, city = 'Kathmandu', mob = 5675765)
