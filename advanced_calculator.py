"""
Advanced Calculator Module
This module provides advanced mathematical operations such as power, square root, and factorial.
"""
import math

def power(base: float, exponent: float) -> float:
    """Returns base raised to the power of exponent."""
    return math.pow(base, exponent)

def square_root(x: float) -> float:
    """Returns the square root of x. Raises ValueError if x is negative."""
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    return math.sqrt(x)

def factorial(n: int) -> int:
    """Returns the factorial of a non-negative integer n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    return math.factorial(n)

if __name__ == "__main__":
    print("Advanced Calculator Demo:")
    print(f"2^10 = {power(2, 10)}")
    print(f"√16 = {square_root(16)}")
    print(f"5! = {factorial(5)}")
