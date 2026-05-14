# #  @decrator name

# def decor(func):
#     def warpper(name):
#         if name == "Gamana":
#             print(f"{name}, Likes KFC")
#         else:
#             return func(name)    
#     return warpper    


# @decor
# def process(name):
#     print(f"{name}, Likes Biriyani")

# process("Nithin")
# process("Chandu")
# process("Gamana") # Gamana, likes KFC
# process("Abhi")


# Technical problem

def smartdiv(function):
    def inner(a, b):
        if b == 0:
            print("Division by 0 is not possible")
        else:
            return function(a, b)
    return inner    
            
@smartdiv            
def div(a, b):
    print(a / b)

div(10, 2)
div(10, 5)
div(10, 0)
