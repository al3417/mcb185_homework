import math

def factorial(n):
	if n == 0: return 1
	fac = 1
	for i in range(1, n + 1):
		fac = fac * i
	return fac

def poi(n, k):	# n is avg occurance, k is number of occurance
	return (((n ** k) * (math.e ** (-n)))/factorial(k))

print(poi(10, 20))
print(poi(10, 10))
print(poi(10, 0))
