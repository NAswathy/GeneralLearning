import numpy as np
l= [1,4,3,6,7,25,16]
print ([x for x in l if x%2==0])
print ([x**2 if x%2==0 else "Not even" for x in l])

l2=[2,5,1,7,10,4,5]
print (sum([x for x in l2 if str(x).isdigit()])) 
print (np.sum(np.array(l2)))
print (sum(l2))


print ("Hello\" world")
print ("Hello"," world", sep="---")
print ("Hello world", end="::::")
print ("Hello there")
name="Aswathy"
title="Ms"
ageLimit=18
print (f"Hello {title}.{name}! How are you?")
print ("Hello {title}.{name}! How are you?".format(title=title, name=name))
print ("Hello %s.%s! Are you above %d?" % (title, name, ageLimit))

def add(a, b):
    return a + b    

a=input("Enter first number: ")
b=input("Enter second number: ")

try:
    result = add(int(a), int(b))
    print(f"The sum of {a} and {b} is: {result}")
except ValueError:
   # print("Invalid input. Please enter valid integers.")
   pass


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    else:
        return a / b

try:
    n1= int(input("Enter first number: "))
    n2= int(input("Enter second number: "))
    result = divide(n1,n2)
    print(f"Result: {result}")
except ValueError as e:
    print(f"Error: {e}")   
else:
    
    print("The numbers were fine for division.")
finally:
    print("Execution completed with or without handling errors.")


def studentNames(*names):
    print("Student Names:", names)
    for n in names:
        print (n)

studentNames("Alice", "Bob", "Charlie")

def studentDetails(**details):
    print("Student Details:", details)

studentDetails(name="Alice", age=20, grade="A")

def studentNames1(**kargs):
    print("Student Names:", kargs)

studentNames1(name1="Alice", name2="Bob", name3="Charlie")

def studentNames2(*args, **kwargs):
    print("Student Names (Positional):", args)
    print("Student Details (Keyword):", kwargs)

studentNames2("Alice", "Bob", "Charlie", name="Alice", age=20, grade="A")

def studentDetails1(age,marks, name='Alice'):
    print (name, age, marks)

studentDetails1(15,25, "Abi")
studentDetails1(15,25)

#oops
class Student:

    def __init__(self, name, age, branch, rollno):
        self.name = name
        self.age = age
        self.branch = branch
        self.rollno = rollno
      #  self.display_info()
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}", f"Branch: {self.branch}")

    def displayAge(self):
        return (f"Age: {self.age}")


class RA(Student):
        def __init__(self, name, age, branch, rollno, salary):
            self.salary = salary
            # super() refers to the parent class (Student). Calling its
            # __init__() reuses the parent initialization code instead of
            # duplicating assignments for name, age, branch, and rollno.
            super().__init__(name, age, branch, rollno)
        
        def displayRollno(self):
            # Call the parent implementation of display_info() first.
          #  super().display_info()
            print(f"Roll Number: {self.rollno} and Salary: {self.salary}")

        def displaySalary(self):
            print(f"Salary: {self.salary}")

        def display_info(self):
                print(f"Name: {self.name}, Age: {self.age}", f"Branch: {self.branch}, Salary: {self.salary}")


Student1 = Student("Alice", 20, "Computer Science", 101)
Student1.display_info()
print (Student1.rollno)
print(Student1.displayAge())

Student2 = RA("Abi", 25, "Electrical Engineering", 102, 50000)
Student2.display_info()
Student2.displayRollno()
Student2.displaySalary()

words = ["banana", "fig", "cherry", "kiwi", "apple", "grape", "orange"]

print("default   :", sorted(words))                 # default sort
print("by length :", sorted(words,key=len))     # by a computed value
print("longest   :", sorted(words, key=len, reverse=True))

# key takes a function of one item, returning what to sort ON.
print()
print("last char :", sorted(words, key=lambda x:x[-1]))
print (sorted(words[::2], key=lambda x:x[-1])) #sorting only the alternate words in the list
people = [("ana", 30), ("bo", 25), ("cy", 35)]
print()
print("by age    :", sorted(people, key=lambda p: p[1]))
print("by length :", sorted(people, key=lambda p: len(p[0])))

# Sorting dicts by a field.
rows = [{"name": "ana", "score": 91}, {"name": "bo", "score": 78}]
print("by score  :", sorted(rows, key=lambda r: r["score"]))
print("by length of name :", sorted(rows, key=lambda r: len(r["name"])))

# Tuple keys sort by the first, then the second - a tiebreak for free.
print()
data = [("b", 2), ("a", 2), ("c", 1)]
print("count then name:", sorted(data, key=lambda t: (t[1], t[0])))
words1 = ["banana", "fig", "cherry", "kiwi", "apple", "grape", "orange"]
print("sorted words1:", sorted(words1))

'''
new = sorted(nums)  # a new list, original untouched
nums.sort()         # rearranges in place, returns None

.sort() exists only on lists. sorted() accepts any iterable. A tuple, a string, a set, a dict (giving its keys). And always hands back a list.
'''

prices = {"apple": 3, "fig": 5}

# [] raises on a missing key; get returns None or a default.
print("prices['apple'] :", prices["apple"])
try:
    prices["kiwi"]
except KeyError as e:
    print("prices['kiwi']  -> KeyError", e)
print("get('kiwi')     :", prices.get("kiwi"))
print("get with default:", prices.get("kiwi", 0))

# Iterating: keys, values, or both.
print()
print("keys  :", list(prices.keys()))
print("values:", list(prices.values()))
for k, v in prices.items():
    print(f"  {k:6} {v}")

# Plain iteration gives keys.
print()
print("for k in prices ->", [k for k in prices])


# Counting: the dance, then the two shortcuts.
words = ["a", "b", "a", "c", "a"]

counts = {}
for w in words:
    if w in counts:
        counts[w] += 1
    else:
        counts[w] = 1
print("if/else   :", counts)

counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
print("get       :", counts)

from collections import Counter
print("Counter   :", dict(Counter(words)))

# Grouping: setdefault returns the value, creating it if absent.
print()
people = [("eng", "ana"), ("ops", "bo"), ("eng", "cy")]
teams = {}
for team, name in people:
    teams.setdefault(team, []).append(name)
print("setdefault:", teams)

# pop removes and returns; update merges.
print()
d = {"a": 1, "b": 2}
print("pop('a')  :", d.pop("a"), "->", d)
print("pop missing with default:", d.pop("zz", "none"))
d.update({"c": 3})
print("update    :", d)
print("merge with |:", {"a": 1} | {"b": 2})
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merged = dict1 | dict2
print(merged)

tup=([1,2,3], [4,5,6],7,8)
print (tup[0][1], tup[1][2], tup[2], tup[3])
tup[0][0]=10
print(tup)

a,b=1,2
### a,b is also a tuple, though not grouped by ()
print (type((5,)))
print (type((5)))

line = "hello"
print(f"{line!r:16} ->{'Myname'}")
print(f"{line:16} ->{'Myname'}")
#output 'hello'          ->Myname # !r is for repr() representation, which includes quotes around the string. The :16 specifies a minimum width of 16 characters, so the output is right-padded with spaces to meet that width.

x=[1,4,2,8,3]

def squares(x):
    for i in x:
        yield i**2
import pandas as pd

df= pd.DataFrame(data=x, columns=['Numbers'])
df['Squares'] = df['Numbers'].applylist(squares(x))