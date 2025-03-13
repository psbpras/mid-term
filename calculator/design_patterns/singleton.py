# design_patterns/singleton.py
"""
Singleton Pattern for a centralized logging system.
"""

import logging
import os

class LoggerSingleton:
    """Singleton logger to ensure a single logging instance throughout the application."""

    _instance = None

    @staticmethod
    def get_instance():
        """Static access method to get the logger instance."""
        if LoggerSingleton._instance is None:
            LoggerSingleton()
        return LoggerSingleton._instance

    def __init__(self):
        """Initializes the logging configuration."""
        if LoggerSingleton._instance is not None:
            raise Exception("Logger is a singleton! Use get_instance().")
        else:
            log_level = os.getenv("LOG_LEVEL", "INFO").upper()
            log_file = os.getenv("LOG_FILE", "app.log")

            logging.basicConfig(
                filename=log_file,
                level=getattr(logging, log_level, logging.INFO),
                format="%(asctime)s - %(levelname)s - %(message)s"
            )
            LoggerSingleton._instance = logging.getLogger("CalculatorLogger")

