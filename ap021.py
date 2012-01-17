def d(n):
	cnt = 0
	for i in range(1, n, 1):
		if(n%i==0):
			cnt += int(i)
	return cnt

def am(max):
	s = 0
	for n in range(1, max, 1):
		if(n == d(d(n)) and n != d(n)):
			s += n
	return s

if __name__ == '__main__':
	print("Sum is: %s" % am(10000))