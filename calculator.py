def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Can't divide by zero"
    else:
        return x / y

def is_number(input_str):
    try:
        float(input_str)
        return True
    except ValueError:
        return False

while True:
    operation = input("Enter operation type: ")

    if operation in ('+', '-', '/', '*'):
        num1_str = input("Enter first digit: ")
        num2_str = input("Enter second digit: ")

        if is_number(num1_str) and is_number(num2_str):
            num1 = float(num1_str)
            num2 = float(num2_str)

            if operation == '+':
                print("Result: ", add(num1, num2))
            elif operation == '-':
                print("Result: ", subtract(num1, num2))
            elif operation == '*':
                print("Result: ", multiply(num1, num2))
            elif operation == '/':
                print("Result: ", divide(num1, num2))
        else:
            print("Error: enter correct digit")
    else:
        print("Error: enter correct operation")