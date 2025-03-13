"""Unit tests for the AdvancedOperations class."""

import math
import pytest
from plugins.advanced_operations import AdvancedOperations  # Ensure correct import


def test_power():
    """Test the power function."""
    assert AdvancedOperations.power(2, 3) == 8
    assert AdvancedOperations.power(5, 0) == 1
    assert AdvancedOperations.power(10, -1) == 0.1
    assert AdvancedOperations.power(-2, 3) == -8
    with pytest.raises(TypeError):
        AdvancedOperations.power("a", 2)


def test_sqrt():
    """Test the square root function."""
    assert AdvancedOperations.sqrt(4) == 2  # Now correctly calls `sqrt`
    assert AdvancedOperations.sqrt(9) == 3
    assert AdvancedOperations.sqrt(0) == 0
    with pytest.raises(ValueError):
        # Should raise an error for negative numbers
        AdvancedOperations.sqrt(-1)
    with pytest.raises(TypeError):
        AdvancedOperations.sqrt("b")


def test_log():
    """Test the logarithm function."""
    assert AdvancedOperations.log(1) == 0  # Now correctly calls `log`
    assert AdvancedOperations.log(math.e) == 1
    assert AdvancedOperations.log(100, 10) == 2
    with pytest.raises(ValueError):
        AdvancedOperations.log(0)  # Logarithm of zero should raise an error
    with pytest.raises(ValueError):
        # Logarithm of negative numbers should raise an error
        AdvancedOperations.log(-5)
    with pytest.raises(TypeError):
        AdvancedOperations.log("c")
