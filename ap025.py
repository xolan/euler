def depth(n):
	return len(str(n))

def fib(n):
	return (n[len(n)-2]+n[len(n)-1])

n = [1, 1]
digits = 1000
while(depth(n[len(n)-1])) < 1000:
	n.append(fib(n))

print("f(%s) =" % len(n), n[len(n)-1])