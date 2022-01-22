a = 10
print(id(a))

def something():
    a = 9

    x = globals()['a']#use of global() function can access the global variable
    #inside a function locally
    print(id(x))
    print("in func",a)
    print("x:",x)
    print(id(x))

    globals()['a']=15


something()

print("outside",a)
