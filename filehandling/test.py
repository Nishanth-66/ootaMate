file = open("demo.txt", "r")
print(file)
print(file.read())
file.close() # need to close compalsarily if not using with if using with no need to close()

with open ("demo.txt", "r") as f:
    line1 = f.readline()
    line2 = f.readline()
    print(line1)
    print(line2)

with open ("demo.txt", "r") as f:
    lst = f.readlines() # stored in a form of readlines
    print(lst)    

with open("demo1.txt", "w") as file:
    file.write("My name is Nishanth")

with open("demo1.txt", "w") as file:
    file.write(" My name is Gamana")


with open("demo1.txt", "a") as file:
    file.write("\nMy name is Nishanth")

# r+ - read and write

with open("demo1.txt", "r+") as file:
    print("Before writing: ", file.read())
    file.seek(7)
    file.write("\nHello Python")
