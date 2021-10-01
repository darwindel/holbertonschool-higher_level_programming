#!/usr/bin/python3
def no_c(my_string):
    c_none = "".join([char for char in my_string if char not in "Cc"])
    return c_none
