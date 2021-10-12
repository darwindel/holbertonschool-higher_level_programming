#!/usr/bin/python3
"""
    Adds 2 integers
    Returns addition of a and b
"""


def add_integer(a, b=98):
    """
    Raises TypeError: if either a or b is a non-int/float
    Returns the addition of a and b
    """
    if not isintance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isistance(b, float):
        raise TypeError("b must be an integer")
    return a + b
