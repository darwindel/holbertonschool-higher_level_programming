#!/usr/bin/python3
"""8-json_api.py"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        data = {'q': ''}
    elif len(sys.argv) > 1:
        data = {'q': sys.argv[1]}

    try:
        req = requests.post('http://0.0.0.0:5000/search_user', data)
        if req.json():
            print('[{}] {}'.format(req.json().get('id'),
                                   req.json().get('name')))
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
