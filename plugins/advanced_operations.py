# plugins/advanced_operations.py
"""
Plugin providing advanced mathematical operations.
"""

import math


class AdvancedOperations:
    """Class containing advanced mathematical operations as static methods."""

    @staticmethod
    def sqrt(x):  # Match the test function names
        """Returns the square root of x."""
        if x < 0:
            raise ValueError(
                "Cannot compute square root of a negative number.")
        return math.sqrt(x)

    @staticmethod
    def power(base, exponent):
        """Returns base raised to the power of exponent."""
        return math.pow(base, exponent)

    @staticmethod
    def log(x, base=math.e):  # Match the test function names
        """Returns the logarithm of x with the specified base."""
        if x <= 0:
            raise ValueError("Logarithm undefined for non-positive values.")
        return math.log(x, base)
