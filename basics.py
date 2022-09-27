"""
    This is multiline
    comment
"""

# Casting

x1 = str(3)
y1 = int(3)
z1 = float(3)

print(type(x1))
print(type(y1))
print(type(z1))

# Many Values to Multiple Variables

x2, y2, z2 = "Orange", "Banana", "Cherry"
print(x2)
print(y2)
print(z2)

# One Value to Multiple Variables

x3 = y3 = z3 = "RED"
print(x3)
print(y3)
print(z3)

# Unpack a Collection

fruits = ["apple", "banana", "cherry"]
x4, y4, z4 = fruits
print(x4)
print(y4)
print(z4)

x5 = "awesome"

def myFunc1():
    x5 = "fantastic"
    print("Python is " + x5)

myFunc1()

print("Python is " + x5)

def myFunc2():
    global x6
    x6 = "fantastic"

myFunc2()

print("Python is " + x6)

"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType

"""

from concurrent.futures import wait
import random

print(random.randrange(1, 10))

x7 = int(1)
y7 = int(2.8)
z7 = int("3")

print(x7, y7, z7)

x8 = float(1)
y8 = float(2.8)
z8 = float("3")
w = float("4.2")

print(x8, y8, z8, w)

x9 = str("s1")
y9 = str(2)
z9 = str(3.0)

print(x9, y9, z9)

w2 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(w2)

w3 = "Hello World"
print(w3[1])

for x in "banana":
    print(x)

print(len(w3))

text1 = "Nothing is best"
print("is " in text1)

if "is " in text1:
    print("Yes, 'is' is present.")

print("expensive" not in text1)

text2 = "Hello, World!"
print(text2[2:5]) # 5 not included
print(text2[2:])
print(text2[:5])

print(text2[-5:-2])

print(text2.upper())
print(text2.lower())
print(text2.strip())
print(text2.replace("H", "J"))
print(text2.split(","))
print(text1 + text2)

quantity = 3
itemno = 567
price = 49.95
order = "I want {} pieces of item {} for {} dollars."
print(order.format(quantity, itemno, price))
order = "I want {2} pieces of item {0} for {1} dollars."
print(order.format(quantity, itemno, price))

text3 = "We are the so-called \"Vikings\" from the north"
print(text3)

"""
    capitalize()
    count("a") Counts of a in string
    find("a")
    format()
    isalnum()
    isalpha()
    islower()
    lower()
    upper()
    replace()
    split()
    strip()
"""

print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("a is greater than b")

print(bool("Hello"))
print(bool(15))

print(bool(False), bool(None), bool(0), bool(""), bool(()), bool([]), bool({}))

class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))

print(isinstance(a, int))

"""
    + - * / %
    ** Exponentiation
    // Floor Devision

    and or not

    is is not

    in not in
"""

# List, Tuple, Set, Dictionary

# LIST

# Ordered, Changeable, Duplicates

"""
    append()
    clear()
    copy()
    count("a")
    extend(["a", "b"])
    index("a")
    insert(1, "a")
    pop(1) pop()
    reverse()
    sort()
"""

thislist = ["apple", "banana", "cherry"]
print(thislist)
print(len(thislist))
thislist1 = list(("apple", "banana", "cherry"))
print(thislist1)
print(thislist[0])
print(thislist[-1])
print(thislist[1:3])

if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

thislist[1] = "blackcurrant"
thislist2 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist2[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist.insert(2, "watermelon")
print(thislist)

thislist.append("orange")

tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

thislist.remove("banana")
thislist.pop()
thislist.pop(1)

del thislist[0]
print(thislist)
del thislist

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

for i in range(len(thislist)):
    print(thislist[i])

while i < len(thislist):
    print(thislist[i])
    i = i + 1

# Looping Using List Comprehension
a = [x for x in thislist]
print(a)

a = [x for x in thislist if "a" in x]
print(a)

thislist.sort()
print(thislist)
thislist.sort(reverse = True)
print(thislist)

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

thislist.reverse()

mylist = thislist.copy()
mylist = list(thislist)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# TUPLE

# Ordered, Unchangeable, Duplicates

thistuple = ("apple", "banana", "cherry")
print(thistuple)
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits

print(green, yellow, red)

(green, *tropic, red) = fruits
print(green, tropic, red)

# SET

# Unordered, Unchangeable, Duplicates

# Dont has indexed

thisset = {"apple", "banana", "cherry"}
print(thisset)


# DICTIONARY

# 3.7 Ordered, 3.6 and earlier Unordered, Changeable, No Duplicates

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(thisdict)
print(thisdict["brand"])
print(len(thisdict))
print(thisdict.get("model"))

x = thisdict.keys()
y = thisdict.values()
x = thisdict.items()

thisdict.update({"year": 2020})

thisdict.pop("model")
thisdict.clear()

for x in thisdict:
    print(x)

for x, y in thisdict.items():
    print(x, y)

# Lambda

x = lambda a: a + 10
print(x(5))

x = lambda a, b: a * b
print(x(5, 6))


# CLASS

class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}({self.age})"

    def myFunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
print(p1)
p1.myFunc()

p1.age = 40
del p1.age
del p1

# class Person:
#     pass

class Student(Person):
    def __init__(self, name, age, rollno):
        Person.__init__(name, age)
        self.rollno = rollno


# from mymodule import person1

# FILE HANDLING

"""
    Read - 'r'
    Write - 'w'
    Append - 'a'
    Create - 'x'
"""

file1 = open("demofile.txt", "r")

print(file1.read())
print(file1.read(5)) # Initial 5 characters
print(file1.readline())

for x in file1:
    print(x)

file1.close()

file2 = open("demofile.txt", "a")
file2.write("Now the file has more content")

import os

if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")

if not os.path.exists("myfile.txt"):
    file3 = open("myfile.txt", "x")

# os.rmdir("myfolder")

try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
else:
    print("Nothing went wrong")
finally:
    print("The 'try except' is finished")

# x = -1
# if x < 0:
#     raise Exception("Sorry, no numbers below zero")

username = input("Enter username")
print("Username is : ", username)

import re

text = "The rain in Spain"
x = re.search("^The.*Spain$", text)
y = re.findall("ai", text)

print(x, y)