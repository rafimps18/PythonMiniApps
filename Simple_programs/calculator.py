num1 = input("Enter a whole number: ")
num2 = input("Enter another whole number: ")
operation = input("Enter...\n + for addition\n - for subtraction\n * for addition\n / for division \n")

def addition(x, y):
    sum = int(x) + int(y)
    return(print("The sum of " + str(x) + " and " + str(y) + " is " + str(sum) + "."))

def subtraction(x, y):
    difference = int(x) - int(y)
    return(print("The difference of " + str(x) + " and " + str(y) + " is " + str(difference) + "."))

def multiplication(x, y):
    product = int(x) * int(y)
    return(print("The sum of " + str(x) + " and " + str(y) + " is " + str(product) + "."))

def division(x, y):
    qoutient = int(x) / int(y)
    return(print("The sum of " + str(x) + " and " + str(y) + " is " + str(qoutient) + "."))

if operation == "+":
    addition(num1, num2)
elif operation == "-":
    subtraction(num1, num2)
elif operation == "*":
    multiplication(num1, num2)
elif operation == "/":
    division(num1, num2)
else:
    print("Invalid symbol.")