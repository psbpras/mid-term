# design_patterns/__init__.py
"""
Design Patterns package initialization.
This module contains implementations of various design patterns used in the project.
"""

from .facade import HistoryFacade
from .factory import OperationFactory
from .singleton import LoggerSingleton
from .strategy import Addition, Subtraction, Multiplication, Division
