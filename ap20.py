n = 100

faclist = []
for x in range(n, 0, -1):
	faclist += [x]

facsum = 1
for x in faclist:
	facsum *= x

sum = 0
for x in str(facsum):
	sum += int(x)

print(sum)