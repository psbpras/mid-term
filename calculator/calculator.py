# calculator/calculator.py

class Calculator:
    """Core calculator class implementing basic arithmetic operations."""

    def add(self, a: float, b: float) -> float:
        """Returns the sum of two numbers."""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Returns the difference of two numbers."""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Returns the product of two numbers."""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """Returns the quotient of two numbers, handling division by zero."""
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b
