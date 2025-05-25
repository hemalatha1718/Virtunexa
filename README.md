# Virtunexa
My internship at Virtunexa on Python development 
Part 1: Calculator Console Application with Logging 
Code : 
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
    print(f"Logging operation to: {filepath}")
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
            log_operation(command, num1, num2, result)

        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()

Execution & output:--


Part 2: Optional GUI with Tkinter : 
Code : -
import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        op = operation.get()

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                raise ValueError("Cannot divide by zero")
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid operation")
            return

        label_result.config(text=f"Result: {result}")
    except ValueError as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

root = tk.Tk()
root.title("Simple Calculator")

tk.Label(root, text="Number 1:").grid(row=0, column=0)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1)

tk.Label(root, text="Number 2:").grid(row=1, column=0)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1)

tk.Label(root, text="Operation (+, -, *, /):").grid(row=2, column=0)
operation = tk.StringVar()
entry_op = tk.Entry(root, textvariable=operation)
entry_op.grid(row=2, column=1)

btn_calc = tk.Button(root, text="Calculate", command=calculate)
btn_calc.grid(row=3, column=0, columnspan=2)

label_result = tk.Label(root, text="Result:")
label_result.grid(row=4, column=0, columnspan=2)

root.mainloop()

Execution and output :- 


Part 3: Text-Based Adventure Game 
Code : - 
def start_game():
    print("Welcome to the Adventure Game!")
    inventory = []

    def first_room():
        print("\nYou are in a dark room. There is a door to your left and right.")
        choice = input("Which door do you take? (left/right) ").lower()
        if choice == 'left':
            left_room()
        elif choice == 'right':
            right_room()
        else:
            print("Invalid choice.")
            first_room()

    def left_room():
        print("\nYou found a key!")
        inventory.append('key')
        print(f"Inventory: {inventory}")
        first_room()

    def right_room():
        print("\nYou meet a dragon!")
        if 'key' in inventory:
            print("You use the key to open a treasure chest and win!")
        else:
            print("You have no weapon and the dragon defeats you. Game Over.")
        quit()

    first_room()

if __name__ == "__main__":
    start_game()

Execution & output :- 



