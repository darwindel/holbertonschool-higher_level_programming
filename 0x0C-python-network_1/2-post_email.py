#!/usr/bin/python3

import urllib.request
import sys

if __name__ == "__main__":
    email = sys.argv[2]
    data = urlib.parse.urlencode(({"email": email}).encode('ascii'))
    with urllib.request.urlopen(sys.argv[1], data) as url:
        s = url.read()
        print(s.decode('utf-8'))
