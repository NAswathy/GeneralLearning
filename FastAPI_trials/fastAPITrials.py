from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class AvailableCuisines(str, Enum):
    indian_menu = "indian_menu"
    italian_menu = "italian_menu"
    mexican_menu = "mexican_menu"


@app.get("/hello")
async def hello():
    return  "Welcome to the Menu API"


menu= {'indian_menu' : ['dosa', 'idli', 'vada'],
              'italian_menu' : ['pizza', 'pasta', 'risotto'],
              'mexican_menu' : ['tacos', 'burritos', 'quesadillas']}

@app.get("/read_menu")

async def read_menu():
    
    return str(menu)




valid_cuisines = set(menu.keys())

@app.get("/read_menu/{cuisine}")
async def read_menu(cuisine: AvailableCuisines):
    
        return menu[cuisine]

    

