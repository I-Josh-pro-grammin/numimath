"""Core mathematical and statistical operations module for numimath."""

from typing import Sequence


def add(a: float, b: float) -> float:
    """Return the sum of two numbers.

    Args:
        a: The first term.
        b: The second term.

    Returns:
        Sum of a and b as a float.
    """
    return float(a + b)


def subtract(a: float, b: float) -> float:
    """Return the difference of two numbers (a - b).

    Args:
        a: The minuend.
        b: The subtrahend.

    Returns:
        Difference of a and b as a float.
    """
    return float(a - b)


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers.

    Args:
        a: The multiplicand.
        b: The multiplier.

    Returns:
        Product of a and b as a float.
    """
    return float(a * b)


def divide(a: float, b: float) -> float:
    """Return the quotient of a divided by b.

    Args:
        a: The dividend.
        b: The divisor.

    Returns:
        Quotient of a / b as a float.

    Raises:
        ZeroDivisionError: If b is equal to zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return float(a / b)


def mean(numbers: Sequence[float]) -> float:
    """Calculate the arithmetic mean of a sequence of numbers.

    Args:
        numbers: A sequence of numeric values (list, tuple, etc.).

    Returns:
        Arithmetic mean of the numbers as a float.

    Raises:
        ValueError: If the input sequence is empty.
    """
    if not numbers:
        raise ValueError("Cannot calculate mean of an empty sequence.")
    return float(sum(numbers) / len(numbers))


def median(numbers: Sequence[float]) -> float:
    """Calculate the median value of a sequence of numbers.

    Args:
        numbers: A sequence of numeric values.

    Returns:
        Median value as a float.

    Raises:
        ValueError: If the input sequence is empty.
    """
    if not numbers:
        raise ValueError("Cannot calculate median of an empty sequence.")
    
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2

    if n % 2 == 1:
        return float(sorted_nums[mid])
    else:
        return float((sorted_nums[mid - 1] + sorted_nums[mid]) / 2.0)


def percentage(part: float, total: float) -> float:
    """Calculate what percentage part is of total.

    Args:
        part: The partial quantity.
        total: The total base quantity.

    Returns:
        Percentage representation (e.g., 25.0 for 25%).

    Raises:
        ZeroDivisionError: If total is equal to zero.
    """
    if total == 0:
        raise ZeroDivisionError("Total cannot be zero when calculating percentage.")
    return float((part / total) * 100.0)


def range_span(numbers: Sequence[float]) -> float:
    """Calculate the difference between the maximum and minimum values in a sequence.

    Args:
        numbers: A sequence of numeric values.

    Returns:
        The range span (max - min) as a float.

    Raises:
        ValueError: If the input sequence is empty.
    """
    if not numbers:
        raise ValueError("Cannot calculate range span of an empty sequence.")
    return float(max(numbers) - min(numbers))
