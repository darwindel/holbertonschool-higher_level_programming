#!/usr/bin/python3
"""sends url req"""
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as url:
        h = url.getheader('X-Request_Id')
        print("{}".format(h))
