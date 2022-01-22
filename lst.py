lst = []


def count(lst):
    string =[]
    less=[]
    for i in lst:
        if(len(i)>=5):
            string.append(i)
        else:
            less.append(i)
    return string,less

x = int(input("Enter your limit:"))
for i in range(x):
    lst.append(input("Enter your name:"))
string,less =count(lst)

print("Strings with more than 5 letters:{}".format(string))
print("String with less than 5 letters:{}".format(less))

