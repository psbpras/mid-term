# calculator/history_manager.py
"""
Manages calculation history using Pandas.
"""

import pandas as pd
import os

class HistoryManager:
    """Handles saving, loading, and clearing calculation history."""

    FILE_PATH = "calculation_history.csv"

    def __init__(self):
        """Initialize history manager and create the file if it doesn't exist."""
        if not os.path.exists(self.FILE_PATH):
            pd.DataFrame(columns=["Operation", "Result"]).to_csv(self.FILE_PATH, index=False)

    def add_entry(self, operation: str, num1: float, num2: float, result: float):
        """Save an operation and result to history."""
        df = pd.DataFrame([[f"{num1} {operation} {num2}", result]], columns=["Operation", "Result"])
        df.to_csv(self.FILE_PATH, mode='a', header=not os.path.exists(self.FILE_PATH), index=False)

    def get_history(self) -> str:
        """Retrieve the history of calculations as a formatted string."""
        if not os.path.exists(self.FILE_PATH):
            return "History is empty."

        df = pd.read_csv(self.FILE_PATH)
        if df.empty:
            return "History is empty."

        return "\n".join(f"{row['Operation']} = {row['Result']}" for _, row in df.iterrows())

    def clear_history(self):
        """Clear the calculation history by removing the file."""
        if os.path.exists(self.FILE_PATH):
            os.remove(self.FILE_PATH)
