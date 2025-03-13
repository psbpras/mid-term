"""This module contains shared fixtures for pytest tests."""

import os
import pytest
from calculator.history_manager import HistoryManager

@pytest.fixture
def history_manager():
    """Fixture to provide a fresh instance of HistoryManager for each test."""
    manager = HistoryManager()
    yield manager
    if os.path.exists(manager.FILE_PATH):
        os.remove(manager.FILE_PATH)
