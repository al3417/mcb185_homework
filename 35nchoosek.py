def factorial(n):
	if n == 0: return 1
	fac = 1
	for i in range(1, n + 1):
		fac = fac * i
	return fac

def nck(n, k):
	return factorial(n) // (factorial(k) * factorial(n - k))

print(nck(50, 10))
print(nck(10, 4))
