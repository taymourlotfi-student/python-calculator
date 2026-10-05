def add(a: float, b: float) -> float:
    """Add two numbers.

    Args:
        a: First number.
        b: Second number.
    Returns:
        The sum of a and b.
    Raises:
        No explicitly raised exceptions.
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract the second number from the first.

    Args:
        a: First number.
        b: Number to subtract.
    Returns:
        The difference between a and b.
    Raises:
        No explicitly raised exceptions.
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers.

    Args:
        a: First number.
        b: Second number.
    Returns:
        The product of a and b.
    Raises:
        No explicitly raised exceptions.
    """
    return a * b


def divide(a: float, b: float) -> float:
    """Divide the first number by the second.

    Args:
        a: Dividend.
        b: Divisor; must not be zero.
    Returns:
        The quotient of a and b.
    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Divisor cannot be zero.")
    return a / b