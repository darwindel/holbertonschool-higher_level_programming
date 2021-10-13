#!/usr/bin/python3

"""Prints "My name is <first_name> <last_name>"""


def say_my_name(first_name, last_name=""):
    """
    Returns a string with the full name
    first_name and last_name must be strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {first_name} {last_name}")
