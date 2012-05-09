#!/bin/env python

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

highest = 0

def con_sum(prime, primelist, index):
    global highest
    sum = 0
    cou = 0
    for p in primelist[:index]:
        if sum < prime:
            sum += p
            cou += 1

    if sum == prime and cou >= highest:
        highest = prime
        print(prime, sum, cou)

if __name__ == '__main__':
    pl = primes(1000000)
    for x, p in enumerate(pl):
        con_sum(p, pl, x)
