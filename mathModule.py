def sum_numbers(a, b):
    """
    Returns the sum of two numbers.
    """
    return a + b


def multiply_numbers(a, b):
    """
    Returns the product of two numbers.
    """
    return a * b


def divide_numbers(a, b):
    """
    Returns the division of two numbers.
    Raises an exception if division by zero is attempted.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
