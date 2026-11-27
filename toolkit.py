# Personal Mini-Toolkit
# PLP Week 8 Final Project

print("===================================")
print(" Welcome to My Personal Mini-Toolkit")
print("===================================")

# List to store tasks
tasks = []

# Main menu loop
while True:
    print("\nPlease choose a tool:")
    print("1. Simple Calculator")
    print("2. To-Do List Manager")
    print("3. Number Guessing Game")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    # Tool 1: Simple Calculator
    if choice == "1":
        print("\n--- Simple Calculator ---")

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        operation = input("Enter your operation (1-4): ")

        if operation == "1":
            result = num1 + num2
            print(f"Result: {num1} + {num2} = {result}")

        elif operation == "2":
            result = num1 - num2
            print(f"Result: {num1} - {num2} = {result}")

        elif operation == "3":
            result = num1 * num2
            print(f"Result: {num1} * {num2} = {result}")

        elif operation == "4":
            if num2 != 0:
                result = num1 / num2
                print(f"Result: {num1} / {num2} = {result}")
            else:
                print("Error: Cannot divide by zero.")

        else:
            print("Invalid operation.")

    # Tool 2: To-Do List Manager
    elif choice == "2":
        while True:
            print("\n--- To-Do List Manager ---")
            print("1. Add a task")
            print("2. View tasks")
            print("3. Remove a task")
            print("4. Return to main menu")

            todo_choice = input("Choose an option (1-4): ")

            if todo_choice == "1":
                task = input("Enter your new task: ")
                tasks.append(task)
                print(f"Task '{task}' added successfully!")

            elif todo_choice == "2":
                if len(tasks) == 0:
                    print("Your task list is empty.")
                else:
                    print("\nYour tasks:")
                    for number, task in enumerate(tasks, start=1):
                        print(f"{number}. {task}")

            elif todo_choice == "3":
                if len(tasks) == 0:
                    print("There are no tasks to remove.")
                else:
                    for number, task in enumerate(tasks, start=1):
                        print(f"{number}. {task}")

                    task_number = int(input("Enter the task number to remove: "))

                    if 1 <= task_number <= len(tasks):
                        removed_task = tasks.pop(task_number - 1)
                        print(f"Task '{removed_task}' removed successfully!")
                    else:
                        print("Invalid task number.")

            elif todo_choice == "4":
                print("Returning to the main menu...")
                break

            else:
                print("Invalid choice. Please select 1-4.")

    # Tool 3: Number Guessing Game
    elif choice == "3":
        print("Number Guessing Game is coming soon.")

    # Quit the program
    elif choice == "4":
        print("Thank you for using my toolkit!")
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please select a number from 1 to 4.")