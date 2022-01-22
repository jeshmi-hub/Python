from math import *

side1 = int(input("Enter base:"))
side2 = int(input("Enter perpendicular:"))
side3 = int(input("Enter hypotenuse:"))

py = sqrt(side1**2+side2**2)

if(py==side3):
    print("right-angled")
else:
    print("Not right-angled")
