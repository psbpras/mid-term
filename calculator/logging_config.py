# calculator/logging_config.py

import logging
import os


class LoggingConfig:
    """Singleton logging configuration for the application."""

    _instance = None

    def __new__(cls):
        """Ensures only one instance of the logger exists."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._configure_logging()
        return cls._instance

    def _configure_logging(self):
        """Configures logging settings based on environment variables."""
        log_level = os.getenv("LOG_LEVEL", "INFO").upper()
        log_file = os.getenv("LOG_FILE", "app.log")

        logging.basicConfig(
            level=log_level,
            format="%(asctime)s - %(levelname)s - %(message)s",
            handlers=[logging.FileHandler(log_file), logging.StreamHandler()],
        )
        self.logger = logging.getLogger("AdvancedPythonCalculator")

    def get_logger(self):
        """Returns the configured logger instance."""
        return self.logger


def configure_logging():
    """Function to initialize logging configuration."""
    LoggingConfig()


# Instantiate logging configuration
logger = LoggingConfig().get_logger()
