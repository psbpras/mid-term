# tests/test_history_manager.py

"""
Unit tests for the HistoryManager class.
"""

import os
import pytest
import pandas as pd
from calculator.history_manager import HistoryManager

@pytest.fixture
def _history_manager():
    """Fixture to provide a fresh instance of HistoryManager for each test."""
    manager = HistoryManager()
    yield manager  # Provide instance
    if os.path.exists(manager.FILE_PATH):
        os.remove(manager.FILE_PATH)  # Cleanup file after test

def test_add_entry(_history_manager):
    """Test adding an operation to history."""
    _history_manager.add_entry("+", 2, 2, 4)
    history = pd.read_csv(_history_manager.FILE_PATH)

    assert not history.empty, "History file should not be empty."
    assert history.iloc[-1]["Operation"] == "2 + 2", "Operation format mismatch."
    assert history.iloc[-1]["Result"] == 4.0, "Result mismatch."

def test_clear_history(_history_manager):
    """Test clearing the calculation history."""
    _history_manager.add_entry("*", 3, 3, 9)
    _history_manager.clear_history()

    assert not os.path.exists(_history_manager.FILE_PATH), "History file should be deleted."

def test_get_history_when_empty(_history_manager):
    """Test retrieving history when no history exists."""
    history = _history_manager.get_history()
    assert history == "History is empty.", "Expected 'History is empty.' but got different output."

def test_get_history_with_entries(_history_manager):
    """Test retrieving history when it contains operations."""
    _history_manager.add_entry("+", 2, 3, 5)
    _history_manager.add_entry("-", 10, 7, 3)

    history = _history_manager.get_history()

    assert "2 + 3 = 5" in history, "Expected '2 + 3 = 5' in history output."
    assert "10 - 7 = 3" in history, "Expected '10 - 7 = 3' in history output."
