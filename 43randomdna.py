import math
import sys
import random

num_seq = 6

for n in range(1, num_seq+1):	# range function is exclusive
	print(f'>seq-{n}\n')
	for i in range(1, random.randint(50, 71)):
		print(random.choice('ACGT'), end='')
	print('\n')
