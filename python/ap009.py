abc_pluss = 1000

for b in range(1, int((abc_pluss/2))+1):
	for a in range(1, b):
		if a * a + b * b == ((abc_pluss-b-a) * (abc_pluss-b-a)):
			print(a * b * ((abc_pluss-b-a)))