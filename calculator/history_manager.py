# calculator/history_manager.py
"""
Manages calculation history using Pandas.
"""

import pandas as pd
import os

class HistoryManager:
    """Handles saving, loading, and clearing calculation history."""

    FILE_PATH = "calculation_history.csv"

    @classmethod
    def save_to_history(cls, operation, result):
        df = pd.DataFrame([[operation, result]], columns=["Operation", "Result"])
        df.to_csv(cls.FILE_PATH, mode='a', header=not os.path.exists(cls.FILE_PATH), index=False)

    @classmethod
    def load_history(cls):
        if os.path.exists(cls.FILE_PATH):
            return pd.read_csv(cls.FILE_PATH)
        return pd.DataFrame(columns=["Operation", "Result"])

    @classmethod
    def clear_history(cls):
        if os.path.exists(cls.FILE_PATH):
            os.remove(cls.FILE_PATH)
