#!/usr/bin/python3
'''how to post email'''
import urllib.request
import sys

if __name__ == "__main__":
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('ascii')
    with urllib.request.urlopen(sys.argv[1], data) as email:
        s = email.read()
        print(s.decode('utf-8'))
