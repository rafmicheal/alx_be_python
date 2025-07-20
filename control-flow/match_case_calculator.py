num1 = int(input("Enter the first number: "))
num2 = int(input("Enter ther second number: "))

operation = input(f"Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        result = num1 + num2
        print(f"The result is: {result}")
    case "-":
        result = num1 - num2
        print(f"The result is: {result}")
    case "*":
        result = num1 * num2
        print(f"The result is: {result}")
    case "/":
        result = num1 / num2
        print(f"The result is: {result}")
    case _:
        print("Invalid operation selected")
