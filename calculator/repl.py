# calculator/repl.py

from calculator.history_manager import HistoryManager  # ✅ Ensure this is imported

class CalculatorREPL:
    def __init__(self):
        self.history_manager = HistoryManager()

    def process_input(self, user_input):
        """Parses and evaluates user input, storing it in history."""
        try:
            # Split input into operands and operator (basic parsing)
            parts = user_input.split()
            if len(parts) != 3:
                raise ValueError("Invalid input format. Use: <num1> <operator> <num2>")

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
        """Starts the REPL loop."""
        print("Welcome to the Advanced Python Calculator! Type 'exit' to quit.")

        while True:
            user_input = input("Enter expression: ").strip()
            if user_input.lower() == "exit":
                break

            result = self.process_input(user_input)
            print(f"Result: {result}")

        # Print history before quitting
        print("History:")
        print(self.history_manager.get_history())
        print("Goodbye!")
