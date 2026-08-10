print("Hello, World!")
x = 10
if x > 5:
  print("x is greater than 5")
else:
  print("x is 5 or less")


def greet(name):
  message = "Hello, {}!".format(name)
  print(message)

greet("Alice")
# Example of using %d and format in print statements
def explain_function_usage():
  number = 42
  # Using %d for integer formatting
  print("The number is %d" % number)
  print("The number is %d" % (number + 10))  # Adding 10 to the number before printing
  # Using format method
  print("The number is {}".format(number))

explain_function_usage()



def calculate_area(radius):
  import math
  area = math.pi * (radius ** 2)
  print (str(type(str(area)))+" is the type")
  return str(area)

radius = 5
#print(f"The area of the circle with radius {radius} is {calculate_area(radius):.2f}")
print (f"The area of a circle with radius {radius} is {calculate_area(radius)}")
try:
      result = calculate_area(radius)
      print(f"The area of a circle with radius {radius} is {result}")
except Exception as e:
  print(f"An error occurred: {e}")
finally:
  print("Finished attempting to calculate area.")



from os import name

import requests
from bs4 import BeautifulSoup

def scrape_books():
    url = "http://books.toscrape.com/"
    proxies = {
        "http": "http://your.proxy.address:port",
        "https": "http://your.proxy.address:port"
    }
    headers = { #to mimic the browser
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    # except requests.RequestException as e:
    except Exception as e:
        print(f"Failed to retrieve the page: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.find_all('article', class_='product_pod')
    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text.strip()
        print(f"Title: {title}, Price: {price}")

if __name__ == "__main__":
    scrape_books()

names="Aswathy"
print (f"My name is {names}")
print ("My name is {}".format(names))
print("My name is %s" %names)

if names == "Aswathy":
  print("The name is Aswathy")
elif names == "Alice":
  print("The name is Alice")
else:  
  print("The name is something else")


class Animal:
    def __init__(self, name, legs=4):
        self.name = name
        self.legs = legs

    def speak(self):
        return f"I am an animal named {self.name}"
    
    def move(self):
        return f"{self.name} is moving on {self.legs} legs"
    
class Dog(Animal):
    def speak(self):
        return f"Woof! I am a dog named {self.name}"
    def fetch(self):
        return f"{self.name} is fetching the ball"  
    
class Cat(Animal):
    def speak(self):
        return f"Meow! I am a cat named {self.name}"
    def climb(self):
        return f"{self.name} is climbing the tree" 
class Human(Animal):
    def speak(self):
        return f"Hello! I am a human named {self.name}"
    def work(self):
        return f"{self.name} is working on a project"   
    def move(self):
        return f"{self.name} is walking on 2 legs"

my_dog = Dog("Tomy", 4)
print(my_dog.speak())
print(my_dog.move())
print(my_dog.fetch())

my_cat = Cat("Kithu", 4)
print(my_cat.speak())
print(my_cat.move())
print(my_cat.climb()) 

my_human = Human("Aswathy", 2)
print(my_human.speak())
print(my_human.move())
print(my_human.work())  


num= input("Enter any number to continue...")
if num.isdigit():
    print(f"You entered the number: {num}")
else:
    print("That's not a valid number. Please enter digits only.")

def positional_args(a, b, c):
   return a + b + c

def default_args(a, b=10):
    return a + b

def keyword_args(a, b, c):
   print(f"a: {a}, b: {b}, c: {c}")

def varLenPositional_args(*args):
    print("Positional arguments:", args)

def varLenKeyword_args(**kwargs):
    print("Keyword arguments:", kwargs)


positional_args(1, 2, 3)
default_args(5)
keyword_args(a=1, c=2, b=3)
varLenPositional_args(1, 2, 3, 4, 5)
varLenKeyword_args(name="Alice", age=30, city="New York")
varLenPositional_args(10, 20)
varLenKeyword_args(name="Alex", profession="Engineer")

import random
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

try:
    n1= random.randint(1, 10)
    n2= random.randint(0, 10)  # This can be zero, which will trigger the exception
    print (n1,n2)
    result = divide(n1,n2)
    print(f"Result: {result}")
except ValueError as e:
    print(f"Error: {e}")



num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")   


try:
    result = float(num1)/float(num2)             
    print(f"The result of dividing {num1} by {num2} is: {result}")

except ValueError as e: #ValueError is error due to inappropriate value, in this case due to division by zero or invalid input
    print(f"Error: {e}")
# except Exception as e: #This is a general exception handler to catch any other unforeseen errors
#     print(f"An unexpected error occurred: {e}")
finally:    
    print("Finished attempting to divide the numbers.")

try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
        print(content)
except Exception as e:
    print(f"Error: {e}")


try:    
    with open("sample.txt", "r") as file:
        content = file.read()
        print(content)

except Exception as e:
    print(f"Error: {e}")   
finally:
    print("Finished attempting to read the file.")



class Vehicle:
  #  def __init__(self, name):
    def __init__(self, brand, model, name="Names"):
        wheels = 4 
        self.name = name
        self.brand = brand
        self.model = model

    def start_engine(self):
        return f"The engine of {self.name} is starting"
    def stop_engine(self):
        return f"The engine of {self.name} is stopping"
    def functionality(self):
        return f"{self.name} is a vehicle with brand {self.brand} and model {self.model}"
    

class Car(Vehicle):
    def __init__(self, brand, model="Unknown"):           
        super().__init__(brand, model)  # Call the constructor of the parent class
        self.brand = brand
        self.model = model

    def functionality(self):
        return f" {self.name}car with brand {self.brand} and model {self.model}"
    def start_engine(self):
        return f"The engine of the car {self.model} is starting"
    def stop_engine(self):
        return f"The engine of the car {self.brand} is stopping"
    

class Bike(Vehicle):
    def __init__(self, brand, model):           
        super().__init__(brand, model)  # Call the constructor of the parent class
        self.brand = brand
        self.model = model

    def functionality(self):
        return f"{self.name} is a bike with brand {self.brand} and model {self.model}"  
    def start_engine(self):
        return f"There is no engine for a bike"
    
    # def stop_engine(self):
    #     return f"There is no engine for a bike"     
    
my_car = Car("Toyota", "Camry")
my_car.wheels = 4
print(my_car.functionality())
print(my_car.start_engine())
print(my_car.stop_engine())
print (my_car.wheels)   

my_bike = Bike("Yamaha", "YZF-R3")
my_bike.wheels = 2
print(my_bike.functionality())
print(my_bike.start_engine())
print(my_bike.stop_engine())
print (my_bike.wheels) 

