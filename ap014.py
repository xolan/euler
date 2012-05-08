from clint.textui import progress
from collections import OrderedDict

def even(n):
	return int(n/2)

def odd(n):
	return int((3*n)+1)

def cal(n):
	if(n % 2 == 0):
		return even(n)
	else:
		return odd(n)

table = {}
for n in progress.bar(range(1, 1000001, 1)):
	print()	#bar bug fix

	if(n not in table):
		table[n] = 1
	m = cal(n)

	while m is not 1:
		m = cal(m)
		table[n] += 1
	
	if m == 1: 
		table[n] += 1


print("Produced the following: (ascending order)")
od = OrderedDict(sorted(table.items(), key=lambda t: t[1]))
print(od)