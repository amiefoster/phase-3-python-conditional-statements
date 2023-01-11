#!/usr/bin/env python3

def admin_login(username, password):
    if username.lower() == "admin" and password == "12345": 
        return "Access granted"
    else:
        return "Access denied"

def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif 65 >= temperature >= 40:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    
    return "It's perfect out there!"
def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

# If the operation is one of the following: +, -, *, or /, return the value of calling the operation on the two numbers. Otherwise, output a message saying "Invalid operation!" and return Non

def calculator(operation, num1, num2):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    else:
        print("Invalid operation!")
        return None
