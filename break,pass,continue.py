
#use of break
available = 10

x = int(input("Enter how many packets of nachos you want:"))


i = 1
while i <=x:
    
    if i>available:
        print("OOPS we are out of stock come back tomorrow")
        break

    print("Nachos")
    i+=1
print("Bye and stay safe")


#use of continue
for i in range(1,101):
    if i%3==0 or i%5==0:
        continue#skips the further execution 
    print(i)

print(":)")

#use of pass

for i in range(1,50):
    if(i%2!=0):
        pass#used as placeholer for future code
    else:
        print(i)

print(":(")






