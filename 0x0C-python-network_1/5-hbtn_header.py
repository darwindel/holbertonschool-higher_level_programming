#!/usr/bin/python3
"""Takes URL sends request displays value of variable"""
import requests
import sys
if __name__ == "__main__":
    print("{}".format(requests.get(sys.argv[1]).headers.get("X-Request-Id")))
