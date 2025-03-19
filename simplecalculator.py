def calculate(num1, num2, operation):
    """Performs the selected operation on two numbers."""
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2 if num2 != 0 else "Error: Division by zero is not allowed."
    elif operation == '**':
        return num1 ** num2
    elif operation == '%':
        return num1 % num2 if num2 != 0 else "Error: Modulo by zero isn't allowed."
    else:
        return "Invalid operation. Please enter +, -, *, /, **, or %."

# Loop for continuous calculation
while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /, **, %), or 'q' to quit: ")

        if operation.lower() == 'q':
            print("Calculator exiting. Goodbye!")
            break

        result = calculate(num1, num2, operation)
        print(f"Result: {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")
