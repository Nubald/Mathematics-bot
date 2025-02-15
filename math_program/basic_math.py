"""
Basic Mathematics Module
Contains fundamental mathematical operations and functions.
"""

class BasicMath:
    @staticmethod
    def add(a: float, b: float) -> float:
        """Add two numbers."""
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Subtract b from a."""
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Multiply two numbers."""
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        """
        Divide a by b.
        Raises:
            ZeroDivisionError: If b is zero
        """
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

    @staticmethod
    def power(base: float, exponent: float) -> float:
        """Calculate base raised to the power of exponent."""
        return base ** exponent

    @staticmethod
    def square_root(n: float) -> float:
        """
        Calculate the square root of a number.
        Raises:
            ValueError: If n is negative
        """
        if n < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return n ** 0.5

    @staticmethod
    def absolute_value(n: float) -> float:
        """Calculate the absolute value of a number."""
        return abs(n)
