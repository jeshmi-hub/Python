weight = int(input())
height = float(input())

BMI = weight/(height * height)
print(BMI)
if BMI<18.5:
    print("Underweight")
elif BMI>=18.5 and BMI<25:
     print("Normal")
elif BMI>=25 and BMI<30:
    print("Overweight")
elif BMI>=30:
    print("obesity")


weight = int(input());
height = float(input());
x = weight/float(height*height);
print(x)
if x < 18.5:
    print('Underweight')
if x>=18.5 and x<25:
    print("Normal")
if x >= 25 and x < 30:
   print('Overweight')
if x >= 30:
   print('Obesity')

