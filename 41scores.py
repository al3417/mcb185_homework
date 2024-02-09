# 1 Z-score is abt 2/3 of the data, 2 Z-score is abt 95%
# write a program that generates number drawn from a normal distribution and calc how many of those are 1, 2, or 3 Z-score above the mean
import random

z1 = 0
z2 = 0
z3 = 0
limit = 100000
for i in range(limit):
	r = random.gauss(0.0, 1.0)
	if r > 1: z1 = z1 + 1
	if r > 2: z2 = z2 + 1
	if r > 3: z3 = z3 + 1
print(1 - 2*z1/limit)
print(1 - 2*z2/limit)
print(1 - 2*z3/limit)
