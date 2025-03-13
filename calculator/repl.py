# calculator/repl.py

from calculator.history_manager import HistoryManager


class CalculatorREPL:
    def __init__(self):
        self.history_manager = HistoryManager()

    def display_menu(self):
        """Displays the menu options."""
        print("\n===== Advanced Python Calculator =====")
        print("1. Perform Calculation")
        print("2. View Calculation History")
        print("3. Exit")
        print("======================================")

    def process_input(self, user_input):
        """Parses and evaluates user input, storing it in history."""
        try:
            # Split input into operands and operator (basic parsing)
            parts = user_input.split()
            if len(parts) != 3:
                raise ValueError(
                    "Invalid input format. Use: <num1> <operator> <num2>")

            num1, operator, num2 = parts
            num1, num2 = float(num1), float(num2)

            # Perform operation
            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                if num2 == 0:
                    raise ZeroDivisionError("Cannot divide by zero.")
                result = num1 / num2
            else:
                raise ValueError("Unsupported operator. Use +, -, *, or /.")

            # Store result in history
            self.history_manager.add_entry(operator, num1, num2, result)
            return result

        except Exception as e:
            return f"Error: {e}"

    def start(self):
        """Starts the REPL loop with a menu."""
        print("\nWelcome to the Advanced Python Calculator!")

        while True:
            self.display_menu()
            choice = input("Enter your choice (1-3): ").strip()

            if choice == "1":
                user_input = input("Enter expression (e.g., 2 + 3): ").strip()
                result = self.process_input(user_input)
                print(f"Result: {result}")

            elif choice == "2":
                history = self.history_manager.get_history()
                print("\nCalculation History:")
                print(history if history else "No calculations performed yet.")

            elif choice == "3":
                print("Exiting the calculator. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 3.")
