import os
import logging
import dotenv
from calculator.command import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand
from calculator.calculator import Calculator  # Core calculator logic
from calculator.plugin_manager import PluginManager
from calculator.design_patterns.singleton import LoggerSingleton
from calculator.repl import CalculatorREPL  # Import the class directly

# Load environment variables
dotenv.load_dotenv()
ENV = os.getenv("ENV", "production")

# Configure logging using Singleton Pattern
logger = LoggerSingleton.get_instance()
logger.info(f"Running in {ENV} mode")

# Initialize calculator instance
calculator = Calculator()

# Command pattern dispatcher using Command objects
COMMANDS = {
    "add": lambda a, b: AddCommand(calculator, a, b).execute(),
    "subtract": lambda a, b: SubtractCommand(calculator, a, b).execute(),
    "multiply": lambda a, b: MultiplyCommand(calculator, a, b).execute(),
    "divide": lambda a, b: DivideCommand(calculator, a, b).execute()
}

# Load dynamic plugins for additional operations
PluginManager.load_plugins()

if __name__ == "__main__":
    # Create an instance of CalculatorREPL and start the REPL loop
    repl = CalculatorREPL()
    repl.start()
