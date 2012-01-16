s = 0
for n in range(1, 1001, 1):
	s += n**n
print(str(s)[-10:])