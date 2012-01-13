n = 2**1000
sum = 0
for x in range(len(str(n))):
	sum += int(str(n)[x])

print(sum)