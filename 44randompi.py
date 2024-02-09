import random
import math

def est_pi():
	points_tot = 0
	points_in = 0

	while True:
		x = random.random()
		y = random.random()
		distance = math.sqrt(x**2 + y**2)
		points_tot += 1
		if distance < 1:
			points_in += 1
		pi = (points_in / points_tot) * 4
		print(pi)

est_pi()




