squares = [0,1,4,9,16,25,36,49,64,81]
print(squares[2:6])
print(squares[3:8])
print(squares[0:1])

sqauares = [0,1,4,9,16,25,36,49,64,81]
print(squares[:7])
print(squares[7:])
print(squares[::2])
print(squares[2:8:3])
print(squares[1:-1])


list = [1,1,2,3,5,8,13]
print(list[list[4]])

#sum of consecutive numbers

N = int(input())
sum = 0
for i in range(1, N+1):
    sum+=i
print(sum)
