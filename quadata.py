import csv
import cmath
with open("D:\\jeshmi\\csv_files\\quaddata.csv","r") as file:
    data =list(csv.reader(file))
    for row in data:
        A,B,C=row
        print(row)
        d = ((B**2)-4*A*C)
        if d>0:
            r1=(-B-cmath.sqrt(d))/(2*A) 
            r2=(-B+cmath.sqrt(d))/(2*A)
            print("root1=",r1)
            print("root2=",r2)
        elif d==0:
            r=-B/2*A
            print("root=",r)
        else:
            print("No root")
