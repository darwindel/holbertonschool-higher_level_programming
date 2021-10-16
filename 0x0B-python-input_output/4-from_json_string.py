#!/usr/bin/python3
"""converts json into python object"""
import json


def from_json_string(my_str):
    """converts string to object"""
    return json.loads(my_str)
