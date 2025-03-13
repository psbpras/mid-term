# design_patterns/strategy.py
"""
Strategy Pattern for handling different arithmetic operations dynamically.
"""

class OperationStrategy:
    """Base class for operations."""

    def execute(self, x, y):
        """Executes the operation. Must be overridden."""
        raise NotImplementedError("Subclasses must implement execute()")

class Addition(OperationStrategy):
    """Addition strategy."""
    
    def execute(self, x, y):
        return x + y

class Subtraction(OperationStrategy):
    """Subtraction strategy."""

    def execute(self, x, y):
        return x - y

class Multiplication(OperationStrategy):
    """Multiplication strategy."""

    def execute(self, x, y):
        return x * y

class Division(OperationStrategy):
    """Division strategy."""

    def execute(self, x, y):
        if y == 0:
            raise ValueError("Division by zero is not allowed.")
        return x / y

