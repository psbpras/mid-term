# tests/test_history_manager.py
"""
Unit tests for the HistoryManager class.
"""

import os
import pandas as pd
import pytest
from calculator.history_manager import HistoryManager

@pytest.fixture(autouse=True)
def cleanup_history():
    """Fixture to clear history before and after each test."""
    HistoryManager.clear_history()
    yield  # Run the test
    HistoryManager.clear_history()

def test_save_to_history():
    """Test that saving to history correctly stores operations."""
    HistoryManager.save_to_history("2 + 2", 4)
    history = HistoryManager.load_history()

    assert not history.empty, "History should not be empty after adding an operation."
    assert history.iloc[0]["Operation"] == "2 + 2", "The first operation should be '2 + 2'."
    assert history.iloc[0]["Result"] == 4, "The result should be 4."
