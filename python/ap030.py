#! /usr/bin/env python

from clint.textui import progress

def test(num):
	before = num
	after = 0
	for x in str(num):
		after += int(x)**5
	return before == after

sum = 0
for x in progress.bar(range(2, (2**18))):
	if(test(x)):
		sum += x
		print(x)

print("Sum: %d" % sum)