import math

limit = 101
def triples(limit):
	for i in range(1, limit):
		for j in range(i, limit):
			hyp = math.sqrt(i**2 + j**2) 
			if math.isclose(hyp, hyp // 1): 
				print(i, j, hyp)

triples(limit)
		
