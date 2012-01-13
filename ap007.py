#!/bin/env python

# a fast prime number list 'generator' using a sieve algorithm

def primes(n):
    """
    returns a list of prime numbers from 2 to n
    """
    if n < 2:  return []
    if n == 2: return [2]
    # create a list of odd numbers from 3 to n
    nums = list(range(3, n+1, 2))
    nums_len = (n // 2) - 1 + (n % 2)
    idx = 0
    idx_sqrtn = (int(n**0.5) - 3) // 2
    while idx <= idx_sqrtn:
        nums_idx = (idx << 1) + 3
        for j in range(idx*(nums_idx+3)+3, nums_len, nums_idx):
            # if not a prime replace with zero
            nums[j] = 0
        idx += 1
        while idx <= idx_sqrtn:
            if nums[idx] != 0:
                break
            idx += 1
    # remove all the zero entries
    return [2] + [x for x in nums if x != 0]

plist = primes(2**17)

for x, y in enumerate(plist):
    if x+1 > 9997 and x+1 < 10005:
        if x+1 == 10001:
            print(x+1,y, '<-- Answer')
        else:
            print(x+1,y)
