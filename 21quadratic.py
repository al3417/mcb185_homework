import sys
import math

def quadratic(a, b, c):
	dis = b**2 - (4*a*c)

	if dis < 0:
		sys.exit('error: two complex roots')
	
	return((-b) + math.sqrt(dis)) / (2*a), ((-b) - math.sqrt(dis)) / (2*a)

# x^2 - 2x + 1
print(quadratic(1, -2, 1))	# x=1

# x^2 - 8x + 5
print(quadratic(1, -8, 5))	# x1=7.31662 x2=0.68337

# 4x^2 + 2x + 5
print(quadratic(4, 2, 5))	# No Real Solution


