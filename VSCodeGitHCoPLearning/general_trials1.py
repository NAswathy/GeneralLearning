# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List of words
words = ["apple", "banana", "cherry", "date", "elderberry"]

# List of tuples (name, age)
people = [("Alice", 12), ("Bob", 25), ("Charlie", 10), ("Diana", 28)]

# List of temperatures in Celsius
temps_celsius = [0, 12, 23, 34, 18, -5, 27]

# List of mixed numbers
mixed_numbers = [3, -1, 0, 7, 12, -8, 5]

# List of dictionaries
students = [
    {"name": "John", "score": 85},
    {"name": "Jane", "score": 92},
    {"name": "Dave", "score": 78}
]

n= [i for i in numbers if i % 2 == 0]   
print("Even numbers:", n)

p= [[person,age] for person, age in people if age > 18]
print("People older than 18:", p)

t= [temp for temp in temps_celsius if temp > 20]
print("Temperatures above 20°C:", t)

s= [student for student in students if student["score"] > 80]
print("Students with scores above 80:", s)


import pandas as pd
data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Age": [12, 25, 10, 28],
    "Score": [85, 92, 78, 88]
}
df = pd.DataFrame(data, columns=data.keys(), index=data["Name"])    

data1= [2.6, 3.1, 4.5, 5.0, 6.2,"Alex",5]
df1= pd.DataFrame(data1, columns=["Values"])
print(df)
print(df1)

with open("sample.txt", "w") as file:
    file.write("Hello, this is a sample text file.\n")
    file.write("This file is used for demonstrating file handling in Python.\n")
    file.write("Have a great day!")


with open("sample.txt", "r") as file:
    content = file.readlines()
    for line in content:
        print ("inside with and for block")
        print(line.strip())



