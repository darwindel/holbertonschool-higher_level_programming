#!/usr/bin/python3
"""10-my_github.py"""

import requests
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    req = requests.get('https://api.github.com/user',
                        auth=(user, password))
    print(r.json().get('id'))
