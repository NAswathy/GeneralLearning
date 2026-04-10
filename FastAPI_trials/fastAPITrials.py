from flask import app

from fastapi import FastAPI
from enum import Enum

apps = FastAPI()

class AvailableCuisines(str, Enum):
    indian_menu = "indian_menu"
    italian_menu = "italian_menu"
    mexican_menu = "mexican_menu"


@apps.get("/hello")
async def hello():
    return  "Welcome to the Menu API"


menu= {'indian_menu' : ['dosa', 'idli', 'vada'],
              'italian_menu' : ['pizza', 'pasta', 'risotto'],
              'mexican_menu' : ['tacos', 'burritos', 'quesadillas']}

@apps.get("/read_menu")

async def read_menu():
    
    return str(menu)




valid_cuisines = set(menu.keys())

@apps.get("/read_menu/{cuisine}")
async def read_menu(cuisine: AvailableCuisines):
    
        return menu[cuisine]


code={1:10, 2:20 }


@apps.get("/get_coupon/{code}")

async def get_coupon(code: int):  
    if code == 1:
        return "You get a 10% discount on your order!"
    elif code == 2:
        return "You get a 20% discount on your order!"
    else:
        return "Invalid coupon code. Please try again." 
    

