nums = [45,60,50,43]

for num in nums:
    if num %5 == 0:
        print(num)
    else:
        print("not found")

#prime numbers
prime = int(input("Enter any number:"))

for i in range(2,prime):
    if prime % i == 0:
        print("not prime")
        break
    else:
        print("prime")
        
