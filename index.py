#gmail = input("Enter your id:)
def male(string):
    i = string.index("@")
    j = string.index(".")
    name = string[:i]
    mail = string[i:j]
    print("hello {} you are using {}".format(name,email))

gmail = input("Enter your id:")

name = gmail[:gmail.index("@"):]

domain = gmail[gmail.index("@") + 1: gmail.index("."):]

print("Hello {} you are using {}".format(name,domain))








                  
