# OOP learning

class Vehicle():
    def __init__(self, types,wheels,brand):
        self.types=types
        self.wheels=wheels
        self.brand=brand

    def movement(self):
        return f"{self.types} can move from one palce to another"
    def fuelReq(self):
        return f"{self.types} can move from one palce to another due to some mechanical energy"
    


class Car(Vehicle):
    def __init__(self, types,wheels,brand):
        
        self.types="passenger"
        self.wheels=4
        self.brand=brand

    def movement(self):
        return f"{self.types} can be driven from one palce to another"
    def fuelReq(self):
        return f"{self.types} can move from one palce to another due to fuel ie petrol or diesel burning energy"

    

class Cycle(Vehicle):
    def __init__(self, types,wheels,brand):
        
        self.types="passenger"
        self.wheels=2
        self.brand=brand

    def movement(self):
        return f"{self.types} can be rode from one palce to another"



v= Vehicle("vehicles",0,"Brand")
print (v.movement())

c1=Car("Sedan",4,"Hyundai-Aura")
c2=Car("hackback",4,"Hyundai-i10") 
print (c1.movement())
print (c1.fuelReq())
print (c2.fuelReq())
b1=Cycle("bicycle",2,"Decathlon")
b1.movement()
b1.fuelReq()
