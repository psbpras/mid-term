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

@pytest.mark.usefixtures("cleanup_history")
def test_save_to_history():
    """Test saving an operation to history using pandas."""
    HistoryManager.save_to_history("2 + 2", 4)
    history = HistoryManager.load_history()

    assert not history.empty
    assert history.iloc[-1]["Operation"] == "2 + 2"
    assert history.iloc[-1]["Result"] == 4

@pytest.mark.usefixtures("cleanup_history")
def test_clear_history():
    """Test clearing the calculation history."""
    HistoryManager.save_to_history("3 * 3", 9)
    HistoryManager.clear_history()

    history = HistoryManager.load_history()
    assert history.empty

@pytest.mark.usefixtures("cleanup_history")
def test_load_history_when_empty():
    """Test loading history when no history exists."""
    history = HistoryManager.load_history()

    assert isinstance(history, pd.DataFrame)
    assert history.empty
    assert list(history.columns) == ["Operation", "Result"]
