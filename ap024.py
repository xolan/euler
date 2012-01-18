from itertools import permutations
d = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

answer = ''
cnt = 1
for n in permutations(d, len(d)):
	print(cnt, n)
	if cnt == 1000000:
		answer = n
	cnt += 1
print(answer)