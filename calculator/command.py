# calculator/command.py
"""
Implements the Command Pattern for executing calculator operations.
"""

class Command:
    """Encapsulates an action and its execution."""

    def __init__(self, execute):
        self.execute = execute

    def run(self):
        return self.execute()
