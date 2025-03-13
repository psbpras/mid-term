# design_patterns/factory.py
"""
Factory Pattern to create calculator operations dynamically.
"""


class OperationFactory:
    """Factory class to create different arithmetic operations."""

    @staticmethod
    def get_operation(operation):
        """Returns a function corresponding to the requested operation."""
        operations = {
            "add": lambda x, y: x + y,
            "subtract": lambda x, y: x - y,
            "multiply": lambda x, y: x * y,
            "divide": lambda x, y: x / y if y != 0 else float("inf"),
        }
        # Default to None if not found
        return operations.get(operation, lambda x, y: None)
