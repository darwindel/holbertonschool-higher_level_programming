#!/usr/bin/python3
for n in range(0, 10):
    for x in range(0, 10):
        if n == 8 and x == 9:
                print('89')
        elif n < x:
            print("{:d}{:d},".format(n, x), end=" ")
