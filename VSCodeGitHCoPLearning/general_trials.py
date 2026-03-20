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
    except requests.RequestException as e:
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


