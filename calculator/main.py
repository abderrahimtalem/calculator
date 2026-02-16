def addition(x, b):
    return x + b      
def subtraction(x, b):
    return x - b
def multiplication(x, b):
    return x * b
def division(x, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    else:
        return x / b  
while True:
    x=float(input("enter the first number:"))
    n=input("enter the operator:")
    b=float(input("enter the second number:"))
    if n == "+":
        print(addition(x, b))
    elif n == "-":
        print(subtraction(x, b))
    elif n == "*":
        print(multiplication(x, b))
    elif n == "/":
        print(division(x, b))
    else:
        print("Invalid operator. Please try again.")