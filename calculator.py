import time

def facto(n):
    fact = 1
    for x in range(1,int(n)):
        fact *= x+1

    return fact

while True:
    print("Options")
    print("Enter 'add' to add two numbers")
    print("Enter 'sub' to subtract two numbers")
    print("Enter 'mult' to multiply two numbers")
    print("Enters 'div' to divide two numbers")
    print("Enters 'fact' to get the factorial of a number")
    print("Enter 'quit' to end the program")
    user_input = input(": ")

    if user_input == "quit":
         time.sleep(1)
         break
    elif user_input == "add":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 + num2)
        print("The answer is " + result)
        time.sleep(1)
    elif user_input == "sub":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 - num2)
        print("The answer is " + result)
        time.sleep(1)
    elif user_input == "mult":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 * num2)
        print("The answer is " + result)
        time.sleep(1)
    elif user_input == "div":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 / num2)
        print("The answer is " + result)
        time.sleep(1)
    elif user_input == "fact":
        num1 = float(input("Enter a number: "))
        result = str(facto(num1))
        print("The answer is: " + result) 
        time.sleep(1)
    
    else:
        print("Unknown input")

    time.sleep(1)