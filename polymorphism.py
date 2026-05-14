print("___Method Overriding(Runtime polymorphsim)___")

class Parent:
    def Marry(self):
        print("Marry at the age of 29-30")

class Child(Parent):
    pass
    #def Marry(self):
     #   print("Marry at the age of 30-35")

c = Child()
c.Marry()         

print("___Method Overloading(compiletime polymorphsim)___") # python does not support true method overloading

class Test:
    def add(self, a, b):
        return a + b
    def add(self, a, b, c):
        return a + b + c
    
t = Test()
#print(t.add(2, 4)) error will come
print(t.add(3, 3, 3))

# using *args (Flexible arguments, functional arguments) to acchive method overloading in python

class Math:
    def add(self, *numbers):
        return sum(numbers)
    
m = Math()

print(m.add(2, 3))
print(m.add(2, 4, 6))

# + works for number and Strings
class Numbers:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

n1 = Numbers(10)
n2 = Numbers(20)
print(n1 + n2)

class Student:
    def __init__(self, marks):
        self.marks = marks

    def __add__(self, other):
        return self.marks + other.marks

s1 = Student(85)
s2 = Student(90)
print(s1 + s2)

print("Hi" + "All")


# Duck Typing

class Parrot:
    def fly(self):
        print("Parrot is flying high in the sky!")

class Airplane:
    def fly(self):
        print("Airplane is taking off!")

# Function using duck typing
def make_it_fly(thing):
    thing.fly()

# Creating instances
parrot = Parrot()
airplane = Airplane()

# Passing different objects to the same function
make_it_fly(parrot)   # Output: Parrot is flying high in the sky!
make_it_fly(airplane) # Output: Airplane is taking off!


class Dog:
    def speak(self):
        print("Dog barks")

class Cat:
    def speak(self):
        print("Cat meows")

def make_sound(animal):
    animal.speak()         

make_sound(Dog())
make_sound(Cat())       

