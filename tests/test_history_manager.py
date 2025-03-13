# tests/test_history_manager.py
"""
Unit tests for the HistoryManager class.
"""

import os
import pandas as pd
import pytest
from calculator.history_manager import HistoryManager

@pytest.fixture
def cleanup_history():
    """Fixture to remove history file after tests."""
    yield
    if os.path.exists(HistoryManager.FILE_PATH):
        os.remove(HistoryManager.FILE_PATH)

def test_save_to_history(cleanup_history):
    HistoryManager.save_to_history("2 + 2", 4)
    history = HistoryManager.load_history()
    assert not history.empty
    assert history.iloc[0]["Operation"] == "2 + 2"
    assert history.iloc[0]["Result"] == 4

def test_clear_history(cleanup_history):
    HistoryManager.save_to_history("3 * 3", 9)
    HistoryManager.clear_history()
    history = HistoryManager.load_history()
    assert history.empty
