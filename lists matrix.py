x = [2,4]
x += [6,8]
print(x)
print(x[2]//x[0])

str = "texting a loop"
count = 0

for x in str:
    if(x=='t'):
        count+=1
print(count)

list = [2,3,4,5,6,7]

for x in list:
    if(x%2==1 and x>4):
        print(x)
        break


for i in range(5):
    print("hello!")



