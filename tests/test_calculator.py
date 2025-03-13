"""
Unit tests for the Calculator class.
"""

import pytest
from calculator.calculator import Calculator

def test_add():
    """
    Test addition operation of Calculator.
    """
    assert Calculator.add(2, 3) == 5

def test_subtract():
    """
    Test subtraction operation of Calculator.
    """
    assert Calculator.subtract(5, 3) == 2

def test_multiply():
    """
    Test multiplication operation of Calculator.
    """
    assert Calculator.multiply(2, 3) == 6

def test_divide():
    """
    Test division operation of Calculator.
    """
    assert Calculator.divide(6, 2) == 3

def test_divide_by_zero():
    """
    Test division by zero raises ValueError.
    """
    with pytest.raises(ValueError):
        Calculator.divide(6, 0)
