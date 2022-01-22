words = ['python','fun']
index = 1
words.insert(index,'is')
print(words)


nums = [1,2,3,4]
nums.append(5)
print(nums)

nums = [4,5,6]
msg = "Numbers: {0} {1} {2}".format(nums[0],nums[1],nums[2])
print(msg)

a = "{x}, {y}".format(x=5, y=12)
print(a)

#strings

print(", ".join(["spam", "eggs", "ham"]))
#prints "spam, eggs, ham"

print("Hello ME".replace("ME", "world"))
#prints "Hello world"

print("This is a sentence.".startswith("This"))
# prints "True"

print("This is a sentence.".endswith("sentence."))
# prints "True"

print("This is a sentence.".upper())
# prints "THIS IS A SENTENCE."

print("AN ALL CAPS SENTENCE".lower())
#prints "an all caps sentence"

print("spam, eggs, ham".split(", "))
#prints "['spam', 'eggs', 'ham']"


def p(word):
    print(word + "!")

p("I")
p("don't")
p("care")

def print_double(x):
    print(2*x)
print_double(3)



def print_numbers():
    print(1)
    print(2)
    return
print(4)
print(6)

def print_nums(x):
    for i in range(x):
        print(i)
        return
print_nums(10)

def func(x):
    res = 0
    for i in range(x):
        res += i
    return res
print(func(4))

#search engine
text = input()
word = input()

def search(text,word):
    if word in text:
        print("Word found")
    else:
        print("Word not found")
search(text,word)
