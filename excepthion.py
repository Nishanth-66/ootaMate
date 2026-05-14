a = int(input("Enter value of a"))
b = int(input("Enter value of b"))
c = [1, 2, 3]

try:
    result = a / b
    print("Result:", result)
except (ZeroDivisionError, ValueError, IndexError, NameError) as e:
    print("Error Occurred:", e)
except:
    print("Error occurred")
finally:
    print("Execution completed !")    

# raise keyword
age = int(input("Enter the age: "))
if age < 0:
    raise ValueError("Age cannot be negative")
print("Your age is: ", age)

def calculate_square_root(number):
    if number < 0:
        raise ValueError("Cannot calculate the square root for negative number")
    return number ** 0.5

try:
    result = calculate_square_root(-9)
    print(f"The result it :,{result}")
except ValueError as e:
    print(f"Error: {e}")


# Custom exception

class InvalidMarksError(Exception):
    pass
try:
   marks = int(input("Enter the marks"))

   if marks < 0 or marks > 100:
    raise InvalidMarksError("Marks should be between 0 to 100")

   print("Marks is : {marks}")

except InvalidMarksError as e:
    print("Custom error", e)   

# Example

Print("Program started")
try:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username != "admin":
        raise Exception("Invalid username")
    if password != "1234":
        raise Exception("Invalid password")
    
    print("Login successful")

except Exception as e:
    print("login failed:", e)

finally:
    print("Program ended")    

