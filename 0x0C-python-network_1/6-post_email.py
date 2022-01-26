#!/usr/bin/python3
"""6-post_email.py"""
import requests
import sys

if __name__ == "__main__":
    email = sys.argv[2]
    request = requests.post(sys.argv[1], data={'email': email})
    print(request.text)
