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

p= [(person,age) for person, age in people if age > 18]
print("People older than 18:", p)


def sum_function(**kwargs):
    total = 0
    for i in kwargs.values():
        total += i

    return total
print ("Sum using kwargs:", sum_function(a=1, b=2, c=3, d=4, e=5, f=6))    

import enum

import pandas as pd
l=[1,1,2,2,2,3,4,1,5,2,7,9,8,6,5,4,3,2,1]
pd.Series(l).value_counts().keys().tolist()[0]

import numpy as np
l=np.random.random_integers(1, 10, 10)
print (l)
print("Boolean array (== 5):", l == 5)

def sum_func_args(*args):
    total = 0
    for i in args:
        total += i

    return total

print ("Sum using args:", sum_func_args(1, 2, 3, 4, 5, 6))

import enum
class calculations(str, enum.Enum):
    add = "add"
    subtract = "subtract"
    multiply = "multiply"
    divide = "divide"

    @staticmethod
    def perform_calculation(a, b, operation):
        if operation == calculations.add:
            return a + b
        elif operation == calculations.subtract:
            return a - b
        elif operation == calculations.multiply:
            return a * b
        elif operation == calculations.divide:
            return a / b if b != 0 else "Error: Division by zero"
        else:
            return "Invalid operation"

# Get user input
print("Available operations:", [op.value for op in calculations])
user_input = input("Enter operation (add, subtract, multiply, divide): ")

try:
    operation = calculations(user_input)
    result = calculations.perform_calculation(10, 5, operation)
    print(f"Result: {result}")
except ValueError:
    print("Invalid operation selected")

