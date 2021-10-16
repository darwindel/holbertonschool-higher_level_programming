#!/usr/bin/python3
"""
append a string at end of text file
"""


def append_write(filename="", text=""):
""" git file to write and append to"""

    with open(filename, "a") as appendfile:
        appendfile.write(text)
    return (len(text))
