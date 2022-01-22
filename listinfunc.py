
more = []

less = []

lst = []



def count(lst):

    for i in lst:

        if len(i) >= 5:

            more.append(i)

        else:

            less.append(i)

    return more, less





x = int(input("Enter the limit:>"))



for i in range(x):

    lst.append(input("Enter the name:>"))



more, less = count(lst)

print("Names with more than 5 characters",more,"\n")

print("Names with less than 5 characters",less)
