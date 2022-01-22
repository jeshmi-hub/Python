lst = []

def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if(i%2==0):
            even+=1
        else:
            odd+=1
    return even, odd



x = int(input("Enter limit:"))

for i in range(x):
        lst.append(int(input("Enter a number:")))

even,odd = count(lst)

print("Even :{}, Odd:{}".format(even,odd))
