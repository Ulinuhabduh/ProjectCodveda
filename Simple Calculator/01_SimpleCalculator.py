def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        print("Cannot divide by zero.")
        return num1
    return num1 / num2

def calculate(num1, num2, operation):
    if operation == '1':
        return add(num1, num2)
    elif operation == '2':
        return subtract(num1, num2)
    elif operation == '3':
        return multiply(num1, num2)
    elif operation == '4':
        return divide(num1, num2)
    else:
        print("Invalid operation.")
        return num1

def calculator():
    print("Select operation.")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    choice = input("Enter choice (1/2/3/4): ")

    result = calculate(num1, num2, choice)
    print(f"Result: {result}")

    while True:
        print("---------------------------------------")
        cont = input("Continue calculation with result? (y/n): ").lower()
        if cont == 'y':
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print('Previous Results:', result)
            choice = input("Enter choice (1/2/3/4): ")
            num2 = int(input("Enter next number: "))
            result = calculate(result, num2, choice)
            print(f"Result: {result}")
        elif cont == 'n':
            print("Calculation finished. Final result:", result)
            break
        else:
            print("Invalid input, exiting.")
            break

calculator()
