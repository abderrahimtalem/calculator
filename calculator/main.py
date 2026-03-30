# --- Python Calculator Project ---
# Created by: Abderrahim Talem
# Description: A robust calculator supporting basic arithmetic operations with error handling.
def addition(num1, num2):
    return num1 + num2      
def subtraction(num1, num2):
    return num1 - num2
def multiplication(num1, num2):
    return num1 * num2
def division(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    else:
        return num1 / num2
while True:
    print("\n--- python calculator ---")
    try:
        num1=float(input("enter the first number:"))
        operator=input("enter the operator (+, -, *, /):")
        num2=float(input("enter the second number:"))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        continue
    if operator == "+":
        print(addition(num1, num2))
    elif operator == "-":
        print(subtraction(num1, num2))
    elif operator == "*":
        print(multiplication(num1, num2))
    elif operator == "/":
        print(division(num1, num2))
    else:
        print("Invalid operator. Please try again.")