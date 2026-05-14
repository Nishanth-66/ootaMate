def add(): #function declaration
    a = 10
    b = 20
    print(a + b)
add()    # function call

def square():
    a = 2
    print(a * a)
square()    

def large(a, b, c):
    if(a > b) :
        print(a)
    elif(b > c):
        print(b)
    else:
        print(c)
        print("Largest of three", large(a, b, c))
large()        

    
