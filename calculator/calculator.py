# calculator/calculator.py
"""
Core calculator functions supporting basic operations.
"""

class Calculator:
    """A simple calculator supporting basic arithmetic operations."""

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
