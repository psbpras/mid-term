# tests/test_repl.py
"""
Unit tests for the REPL class.
"""

import pytest
from calculator.repl import REPL

@pytest.fixture
def mock_input(monkeypatch):
    """Mocks user input for testing."""
    inputs = iter(["2 + 3", "history", "exit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

def test_repl_execution(mock_input, capsys):
    repl = REPL()
    repl.start()
    captured = capsys.readouterr()
    assert "Result: 5" in captured.out
