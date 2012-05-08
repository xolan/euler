#!/bin/env python

#
#   Took about 30mins to run on my netbook... It's really slow, probably due to writes, but it works :P
#   Number of "Fit"'s is the answer.
#

from clint.textui import progress, colored, min_width
import sys

magic = []

def square_add(num, list):
    num = str(num)
    digits = {}
    for i, digit in enumerate(num):
        digits[i] = digit

    sum = 0
    for x in digits:
        sum += int(digits[x]) * int(digits[x])

    list.append(str(sum))
    return list

for i in progress.bar(range(1, 10000000, 1)):
    nums = []
    nums.append(str(i))
    while nums[-1] != '89' and nums[-1] != '1':
        square_add(nums[-1], nums)
    if nums[-1] == '89':
        magic.append(nums[0])
    nums = []
    sys.stderr.write(min_width('Fit [%s] ' % str(len(magic)), len('Fit [%s] ' % str(10000000))))
