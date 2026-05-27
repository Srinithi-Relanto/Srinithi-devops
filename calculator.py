"""
Simple Calculator Module
This module provides basic arithmetic operations.
"""

def add(a: float, b: float) -> float:
    """Returns the sum of a and b."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Returns the difference of a and b."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Returns the product of a and b."""
    return a * b

def divide(a: float, b: float) -> float:
    """Returns the quotient of a and b. Raises ValueError on division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

if __name__ == "__main__":
    print("Calculator Demo:")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"6 * 7 = {multiply(6, 7)}")
    print(f"8 / 2 = {divide(8, 2)}")
