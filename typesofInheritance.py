# 1. Single inheritance
class Vehicle:
    def start(self):
        print("Vehicle Starts")

class Car(Vehicle):
    pass

c = Car()
c.start()

#2. multiple inheritance

class Engine:
    def engine_type(self):
        print("Petrol engine")

class Wheels:
    def wheel_count(self):
        print("4 wheels")

class Car(Engine, Wheels):
    pass
c = Car()
c.engine_type()
c.wheel_count()

#3. multilevel inheritance

class Vehicle:
    def start(self):
        print("Vehicle Starts")

class Car(Vehicle):
    def drive(self):
        print("Car drives")

class SportsCar(Car):
    def speed(self):
        print("Very fast")

s = SportsCar()
s.start()
s.drive()
s.speed()

# 4. Hierarchical Inheritance

class Vehicle:
    def start(self):
        print("Vehicle Starts")

class Car(Vehicle):
    pass

class Bike(Vehicle):
    pass

c = Car()
b = Bike()

c.start()
b.start()

# 5. Hybride Inheritance 

class Vehicle:
    def start(self):
        print("Vehicle Starts")

class Engine(Vehicle):
    def engine(self):
        print("Engine Working")

class Wheels:
    def wheels(self):
        print("Wheel rolling")

class Car(Engine, Wheels):
    pass

c= Car()
c.start()
c.engine()
c.wheels()



