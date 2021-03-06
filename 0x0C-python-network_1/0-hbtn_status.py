#!/usr/bin/python3
""" fetching url """
import urllib.request

with urllib.request.urlopen('https://intranet.hbtn.io/status') as url:
    html = url.read()
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(html.decode('utf-8')))
