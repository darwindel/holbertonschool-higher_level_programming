#!/usr/bin/python3
    '''
    checks if object is an instance of an inherited class
    '''


def inherits_from(obj, a_class):
    '''
    will return true if the object is instance of inherited class
    '''

    return(issubclass(type(obj), a_class) and type(obj) is not a_class)
