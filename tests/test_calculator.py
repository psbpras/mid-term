# tests/test_calculator.py
"""
Unit tests for the Calculator class.
"""

import pytest
from calculator.calculator import Calculator

def test_add():
    assert Calculator.add(2, 3) == 5

def test_subtract():
    assert Calculator.subtract(5, 3) == 2

def test_multiply():
    assert Calculator.multiply(2, 3) == 6

def test_divide():
    assert Calculator.divide(6, 2) == 3

def test_divide_by_zero():
    with pytest.raises(ValueError):
        Calculator.divide(6, 0)
