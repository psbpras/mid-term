"""
Unit tests for the REPL class.
"""

from unittest.mock import patch  # Standard library import (correct position)
from calculator.repl import CalculatorREPL  # Local import (correct position)

@patch("builtins.input", side_effect=["2 + 3", "exit"])
def test_repl_execution(mock_input, capsys):
    """Test REPL execution flow with mock input."""
    _ = mock_input  # Suppress unused argument warning

    repl = CalculatorREPL()
    repl.start()  # Runs REPL loop with mocked input

    captured = capsys.readouterr()

    # Ensure correct output is printed
    assert "Result: 5.0" in captured.out, "Expected 'Result: 5.0' in output."
    assert "History:" in captured.out, "Expected 'History:' in output."
    assert "2.0 + 3.0 = 5.0" in captured.out, "Expected history to contain '2.0 + 3.0 = 5.0'."
