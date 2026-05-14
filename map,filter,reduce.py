
# _______________map()_________________

numbers = [1, 2, 3, 4, 5, 6]

square = []
for x in numbers:
    square.append(x * 2)
print(square)
#________________________________________


def square(x):
    return x * 2

numbers = [1, 2, 3, 4, 5, 6]

squares = list(map(square, numbers))
print(squares)

#__________________________________________ using lambda function

numbers = [1, 2, 3, 4, 5, 6]
squares = list(map(lambda x: x * 2, numbers))
print(squares)

#_____________________filter()_____________________________

numbers = [1, 2, 3, 4, 5, 6]

evens = []
for x in numbers:
    if x in numbers:
        if x % 2 == 0:
            evens.append(x)
print(evens)

#___________________________________________________

def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]

evens = list(filter(is_even, numbers))
print(evens)

#_____________________________________________________ using lambda


numbers = [1, 2, 3, 4, 5, 6]

evens = list(filter(lambda x: x % 2 == 0,numbers))
print(evens)

#_______________reduce()_______________________________

numbers = [1, 2, 3, 4, 5, 6]
total = 0
for x in numbers:
    total = total + x
print(total)

#________________________________________________________

from functools import reduce

def add(a, b):
    return a + b

numbers = [1, 2, 3, 4, 5, 6]

total = reduce(add, numbers)
print(total)

#________________________________________________________using lambda

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

total = reduce(lambda a, b: a + b, numbers)
print(total)