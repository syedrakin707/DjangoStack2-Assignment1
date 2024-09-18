def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

def modulus(num1, num2):
    return num1 % num2

if __name__ == '__main__':
    print("Select Operation")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    operation = input("Enter Choice (1/2/3/4/5): ")
    op = int(operation)
    ops = [1, 2, 3, 4, 5]
    if op in ops:
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))
        if op == 1:
            result = addition(num1, num2)
            print("Addition: {} + {} = {}".format(num1, num2, result))
        elif op == 2:
            result = subtraction(num1, num2)
            print("Subtraction: {} - {} = {}".format(num1, num2, result))
        elif op == 3:
            result = multiplication(num1, num2)
            print("Multiplication: {} * {} = {}".format(num1, num2, result))
        elif op == 4:
            try:
                result = division(num1, num2)
                print("Division: {} / {} = {}".format(num1, num2, result))
            except ZeroDivisionError:
                print("ZeroDivisionError: Cannot be divided by zero")
        elif op == 5:
            result = modulus(num1, num2)
            print("Modulus: {} % {} = {}".format(num1, num2, result))
    else:
        print("Invalid Operation")




