import os

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def log_operation(operation, num1, num2, result):
    filepath = os.path.abspath("history.txt")
    print(f"Logging operation to: {filepath}")  # debug print to confirm logging runs
    with open("history.txt", "a") as f:
        f.write(f"{operation} {num1} {num2} = {result}\n")

def main():
    print("Welcome to the Python Calculator!")
    print("Commands: add, subtract, multiply, divide, quit")

    while True:
        user_input = input("Enter command and two numbers (e.g. add 2 3): ")
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break

        parts = user_input.split()
        if len(parts) != 3:
            print("Invalid input format. Use: command number1 number2")
            continue

        command, num1_str, num2_str = parts

        try:
            num1 = float(num1_str)
            num2 = float(num2_str)
        except ValueError:
            print("Please enter valid numbers.")
            continue

        try:
            if command == "add":
                result = add(num1, num2)
            elif command == "subtract":
                result = subtract(num1, num2)
            elif command == "multiply":
                result = multiply(num1, num2)
            elif command == "divide":
                result = divide(num1, num2)
            else:
                print("Unknown command.")
                continue

            print(f"Result: {result}")
            # THIS IS IMPORTANT: call log_operation here
            log_operation(command, num1, num2, result)

        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
