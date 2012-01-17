from clint.textui import progress

def d(n):
	cnt = 0
	for i in range(1, n, 1):
		if(n%i==0):
			cnt += int(i)
	return cnt

done = []
for n in progress.bar(range(1, 10000, 1), label="Evaluating "):
	if(n == d(d(n)) and n != d(n)):
		done.append(n)

print("Sum is: %s" % sum(done))