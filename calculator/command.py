# calculator/command.py

from abc import ABC, abstractmethod

class Command(ABC):
    """Abstract base class for all calculator commands."""

    @abstractmethod
    def execute(self):
        pass


class AddCommand(Command):
    """Command to perform addition."""

    def __init__(self, calculator, a, b):
        self.calculator = calculator
        self.a = a
        self.b = b

    def execute(self):
        return self.calculator.add(self.a, self.b)


class SubtractCommand(Command):
    """Command to perform subtraction."""

    def __init__(self, calculator, a, b):
        self.calculator = calculator
        self.a = a
        self.b = b

    def execute(self):
        return self.calculator.subtract(self.a, self.b)


class MultiplyCommand(Command):
    """Command to perform multiplication."""

    def __init__(self, calculator, a, b):
        self.calculator = calculator
        self.a = a
        self.b = b

    def execute(self):
        return self.calculator.multiply(self.a, self.b)


class DivideCommand(Command):
    """Command to perform division."""

    def __init__(self, calculator, a, b):
        self.calculator = calculator
        self.a = a
        self.b = b

    def execute(self):
        return self.calculator.divide(self.a, self.b)
