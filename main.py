# main.py
# Entry point for the advanced calculator application

from calculator.repl import REPL

def main():
    """
    Initializes and starts the REPL for user interaction.
    """
    repl = REPL()
    repl.run()

if __name__ == "__main__":
    main()
