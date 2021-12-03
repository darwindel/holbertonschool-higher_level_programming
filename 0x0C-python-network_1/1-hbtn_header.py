#!/usr/bin/python3
"""fetches header"""
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as url:
        header = url.getheader('X-Request-Id')
        print("{}".format(header))
