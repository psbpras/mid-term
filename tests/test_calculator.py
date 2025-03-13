# tests/test_calculator.py
"""
Unit tests for the Calculator class.
"""

import pytest
from calculator.calculator import Calculator

@pytest.fixture
def calculator():
    """Fixture to create a Calculator instance."""
    return Calculator()

def test_add(calculator):
    """Test addition operation."""
    assert calculator.add(2, 3) == 5

def test_subtract(calculator):
    """Test subtraction operation."""
    assert calculator.subtract(5, 3) == 2

def test_multiply(calculator):
    """Test multiplication operation."""
    assert calculator.multiply(2, 3) == 6

def test_divide(calculator):
    """Test division operation."""
    assert calculator.divide(6, 3) == 2

def test_divide_by_zero(calculator):
    """Test division by zero handling."""
    with pytest.raises(ValueError, match="Division by zero is not allowed."):
        calculator.divide(6, 0)
