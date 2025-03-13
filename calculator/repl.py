# calculator/repl.py
"""
Implements the Read-Eval-Print Loop (REPL) for user interaction.
"""

from calculator.calculator import Calculator
from calculator.history_manager import HistoryManager

class REPL:
    """Provides a command-line interface for interacting with the calculator."""

    def start(self):
        print("Advanced Python Calculator - Type 'exit' to quit.")
        while True:
            command = input("> ")
            if command.lower() == "exit":
                break
            elif command.lower() == "history":
                print(HistoryManager.load_history())
            else:
                try:
                    result = eval(command)
                    print(f"Result: {result}")
                    HistoryManager.save_to_history(command, result)
                except Exception as e:
                    print(f"Error: {e}")
