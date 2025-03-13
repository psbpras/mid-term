# design_patterns/facade.py
"""
Facade Pattern for simplified history management using Pandas.
"""

import pandas as pd

class HistoryFacade:
    """A Facade to handle history management with a simple interface."""

    def __init__(self, filename="calculation_history.csv"):
        self.filename = filename

    def save_history(self, data):
        """Saves a new record to the history file."""
        df = pd.DataFrame([data])
        try:
            df.to_csv(self.filename, mode='a', header=not self._file_exists(), index=False)
        except Exception as e:
            print(f"Error saving history: {e}")

    def load_history(self):
        """Loads the calculation history."""
        try:
            return pd.read_csv(self.filename)
        except FileNotFoundError:
            return pd.DataFrame(columns=["Operation", "Operand1", "Operand2", "Result"])

    def _file_exists(self):
        """Checks if the history file exists."""
        try:
            with open(self.filename, "r"):
                return True
        except FileNotFoundError:
            return False

