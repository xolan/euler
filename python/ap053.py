def facToList(n):
	l = []
	for i in range(n, 0, -1):
		l.append(i)
	return l

def fac(l):
	s = 1
	for n in l:
		s *= n
	return s

def nCr(n, r):
	return (int)(fac(facToList(n)) / (fac(facToList(r))*fac(facToList(n-r))))

aboveMill = []
for i in range(1, 101, 1):
	for j in range(i, 0, -1):
		if nCr(i, j) > 1000000:
			aboveMill.append(nCr(i, j))

print(len(aboveMill))