"""
Unit tests for the REPL class.
"""

from unittest.mock import patch
from calculator.repl import CalculatorREPL


# Simulates user choices
@patch("builtins.input", side_effect=["1", "2 + 3", "2", "3"])
# `_` is used for an unused argument to avoid Pylint warnings
def test_repl_execution(_, capsys):
    """Test REPL execution flow with mock input for menu navigation and calculations."""

    repl = CalculatorREPL()
    repl.start()  # Runs REPL loop with mocked input

    captured = capsys.readouterr()  # Capture printed output

    # Check if the menu appears
    assert "===== Advanced Python Calculator =====" in captured.out, "Menu should be displayed."

    # Check calculation output
    assert "Result: 5.0" in captured.out, "Expected 'Result: 5.0' in output."

    # Check history output
    assert "Calculation History:" in captured.out, "Expected history section in output."
    assert "2.0 + 3.0 = 5.0" in captured.out, "Expected '2.0 + 3.0 = 5.0' in history output."

    # Check exit message
    assert "Exiting the calculator. Goodbye!" in captured.out, "Expected exit message in output."
