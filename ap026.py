from operator import itemgetter

def recurring_cycle_length(n):
	cycleLen = 0
	#  remove powers of 2 and 5 in n
	while (n % 2 == 0):
		n /= 2
	while (n % 5 == 0):
		n /= 5
	if n > 1:
		a = 10 % n
		cycleLen = 1
		while a != 1:
			a *= 10
			a %= n
			cycleLen += 1
	return cycleLen

nums = []
for n in range(1, 1000):
	#print(n, 1/n, recurring_cycle_length(n))
	nums.append((n, recurring_cycle_length(n)))
print('\n   d, length')
print(sorted(nums, key=itemgetter(1), reverse=True)[0])
print('\n')