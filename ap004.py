#!/bin/env python

def ispalindrome(word):
    return word == word[::-1]

min = 100
max = 1000 # (999)

palin = []

for x in range(min, max, 1):
    for y in range(min, max, 1):
        if ispalindrome(str(x*y)):
            if not (x*y) in palin:
                palin.append(x*y)

palin.sort()
print(palin)
