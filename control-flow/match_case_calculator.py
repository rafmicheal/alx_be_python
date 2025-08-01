num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        result = int(num1 + num2)
        print(f"The result is {result}.")
    case "-":
        result = int(num1 - num2)
        print(f"The result is {result}.")
    case "*":
        result = int(num1 * num2)
        print(f"The result is {result}.")
    case "/":
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            result = int(num1 / num2)
            print(f"The result is {result}.")
    case _:
        print("Invalid operation selected")
