#! /usr/bin/env python

import math
from clint.textui import progress, puts

def triangle(num):
    tri = 0
    for x in range(1, num+1):
        tri += x
    return tri

def get_divisors(num):
    divs = 0
    for x in range(1, int(math.sqrt(num))):
        if num % x == 0:
            divs += 2
    return divs

def main():
    nums = range(1, 2**16)
    largest = 0
    first = 0
    for n in progress.bar(nums):
        tri = triangle(n)
        len_div = get_divisors(tri)
        if len_div > largest:
            largest = len_div
            puts("[%d, %d, %d" % (n, tri, largest))

if __name__ == '__main__':
    main()
