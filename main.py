# main.py
"""
Entry point for the calculator application.
"""

"""
Entry point for the calculator application.
"""

import sys
import logging
from calculator.logging_config import configure_logging
from calculator.repl import CalculatorREPL

def main():
    """Main function to start the calculator REPL."""
    try:
        configure_logging()
        logger = logging.getLogger("AdvancedPythonCalculator")
        logger.info("Starting the Calculator REPL...")
        
        repl = CalculatorREPL()
        repl.start()

    except Exception as e:
        logging.error(f"Unexpected error: {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()
