import math

def pi(limit):
	pi = 3
	flip = 1
	for i in range(1, limit + 1):
		n = (4 / ((2 * i) * (2 * i + 1) * (2 * i +2))) * flip
		flip = flip * -1
		pi = pi + n
	return pi

print(pi(1))
print(pi(2))
print(pi(3))
print(pi(10))
print(pi(20))
print(pi(30))
print(pi(50))
print(pi(100))

