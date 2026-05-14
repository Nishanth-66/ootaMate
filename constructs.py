# even number
for num in range(1, 11):
    if num % 2 == 0:
        print(num, end=" ") 

#jump control statement 1-6
 #break - 3

for i in range(1, 6):
    if i == 4:
        break
    print(i, end=" ")

for i in range(0, 6):
    if i == 4:
        continue
    print(i, end=" ")

def square(n):
    return n * n
print(square(4), end=" ")

#pass

for i in range(0, 6):
    pass

def add():
    pass
add()