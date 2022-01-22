x = 0

while x <=20:
    print(x)
    x += 2
 #break and continue statements 
i=0
while 1==1:
    print(i)
    i = i+1
    if i>= 5:
        print("Finished")
        break
print("Finished")

i=5

while True:
    print(i)

    i = i-1
    if i <=2:
        break

i = 1
while i<=5:
    print(i)
    i+=1
    if i==3:
        print("Skipping 3")
        continue

while False:
    print("looping")

grade = int (input())
if grade >= 70:
    print("pass")
elif grade <=70:
    print("fail")
else:
    print("i don't study")

i=0
x=0
while i<4:
    print(i)
    x+=i
    i+=1
print(i)
print(x)

    
