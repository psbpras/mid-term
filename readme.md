# Advanced Python Calculator for Software Engineering Graduate Course

#Project structure:


AdvancedPythonCalculator/
│── calculator/
│   │── __init__.py
│   │── calculator.py             # Core calculator functions
│   │── history_manager.py        # Handles history management using Pandas
│   │── logging_config.py         # Centralized logging setup
│   │── repl.py                   # Command-line REPL interface
│   │── command.py                # Implements Command Pattern for REPL commands
│   │── plugin_manager.py         # Dynamically loads plugins
│   │── design_patterns/
│   │   │── __init__.py
│   │   │── facade.py             # Implements Facade Pattern for history management
│   │   │── factory.py            # Implements Factory Pattern for operations
│   │   │── singleton.py          # Implements Singleton Pattern for logging
│   │   │── strategy.py           # Implements Strategy Pattern for different operations
│── plugins/                      # Directory for dynamically loaded plugins
│   │── __init__.py
│   │── advanced_operations.py    # Example plugin for extra operations
│── tests/                        # Unit tests with Pytest
│   │── test_calculator.py
│   │── test_history_manager.py
│   │── test_repl.py
│   │── test_plugin_manager.py
│── .env                          # Environment variables for logging
│── .gitignore
│── README.md                     # Project documentation
│── requirements.txt               # Dependencies (Pandas, Pytest, etc.)
│── main.py                        # Entry point for the calculator application

#Installation

1.  Clone the repository

git clone https://github.com/psbpras/mid-term.git
cd mid-term

2.  Set up a virtual environment

python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

3.  Install dependencies

pip install -r requirements.txt


# Project Overview

This project is an advanced Python-based calculator application developed for the midterm assessment of a software engineering graduate course.
The application integrates professional software development practices, emphasizing clean and maintainable code, design patterns, comprehensive logging, environment variable configuration, and a command-line interface (REPL) for real-time user interaction.


# Features

Command-Line Interface (REPL): Supports real-time user interaction for executing calculations and managing history.

Plugin System: Allows dynamic extension of features without modifying core application logic.

Calculation History Management: Stores and manipulates calculation history using Pandas.

Logging Mechanism: Tracks detailed application operations, errors, and warnings.

Design Patterns Implementation: Utilizes Facade, Command, Factory Method, Singleton, and Strategy patterns for a scalable architecture.

Dynamic Configuration: Uses environment variables for flexible logging levels and output control.

Comprehensive Testing: Ensures 90%+ test coverage with Pytest and follows PEP 8 coding standards.


# Usage Instructions:

1. Start the REpl
	python3 main.py

2. perform calculations
	2 + 3  ( Result = 5)
	2 - 3 ( Result = -1)
3. view available plugins
4. Exit

#Design Patterns and Architectural Decisions

1. Facade Pattern

Used to simplify complex Pandas operations for history management.

Example: HistoryManager acts as a facade to interact with Pandas DataFrames.

2. Command Pattern

Structures commands within the REPL to ensure modularity and scalability.

Example: Each command (add, subtract, multiply) is encapsulated in a Command class.

3. Factory Method Pattern

Allows dynamic creation of new operations without modifying existing code.

Example: The OperationFactory class creates command objects based on user input.

4. Singleton Pattern

Ensures only one instance of the history manager exists to handle calculations.

Example: HistoryManager follows the Singleton pattern.

5. Strategy Pattern

Enables flexible switching of calculation strategies at runtime.

Example: Different calculation strategies can be applied based on user preferences.



#Logging Strategy

Logging Levels: Supports INFO, WARNING, and ERROR based on environment variable settings.

Logging to File: Logs stored in calculator.log for debugging and monitoring.

Implementation Example:

import logging
from dotenv import load_dotenv
import os

load_dotenv()
log_level = os.getenv("LOG_LEVEL", "INFO").upper()
logging.basicConfig(filename=os.getenv("LOG_FILE", "calculator.log"), level=log_level)
logging.info("Calculator started")


#Testing and Code Quality

Testing Framework: Pytest

Test Coverage: Achieves 90%+ coverage.

Linting: Uses Pylint for code quality verification.

Run Tests: 
	pytest
	pytest --pylint
	pytest --pylint --cov


# GitHub Actions (CI/CD)

This project uses GitHub Actions to automatically test the code on every push or pull request. The workflow file is in .github/workflows/ci.yml.

	git push origin main

To check workflow status:

1. Go to your GitHub repository

2. Click on Actions tab

3. Check the latest workflow run

