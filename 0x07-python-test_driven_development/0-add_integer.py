#!/usr/bin/python3
"""
    Adds 2 integers
    Prototype: def add_integer(a, b=98)
    Returns an integer: addition of a and b
"""


def add_integer(a, b=98):
    """
    Raises TypeError: if either a or b is a non-int/float
    Returns the addition of a and b
    """
    if (a is None or not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
