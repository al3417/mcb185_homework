import random

# produce a number that is 0 <= x < 1
for i in range(5):
	print(random.random())

# choose from the container
for i in range(50):
	print(random.choice('ACGT'), end='')
print()

# To generate unequal chance random
for i in range(50):
	r = random.random()
	if r < 0.7: print(random.choice('AT'), end='')	
# base on the previous random number to pick
	else:		print(random.choice('CG'), end='')
print()

# random.randint()
# generate a random number between two inclusive end points
for i in range(3):
	print(random.randint(1, 6))

# random.gauss()
# random base on Gaussian distribution, mean, standard deviation
for i in range(5):
	print(random.gauss(0.0, 1.0))

# Pretty Printing
print('this line\n has some\n line breaks') # \n to make new lines
print('a\tb\tcat\tdogma')	# line up columns of text
print(10, 20, 30, 40, sep='\t')		# seperate values with tabs
print(100, 2000, 30000, 40000, sep='\t')

# f-strings
i = 1
pi = 3.14159
print('normal string {i} {pi}')
print(f'formatted string {i} {pi}')
print(f'tau {pi + pi}')
print(f'formatted string {i} {pi:.3f}') 
# floating point rounding, 3 is 3 digits of precision

# sys.stderr
import sys
print('logging', file=sys.stderr)

# Monte Carlo
# perform repeated random sampling to arrive at a solution
# e.g. to estimate Pi by throwing random darts

# Pseudorandom
# the random number are not 'random' in pc, they are generated using a given staring 'seed'
random.seed(1)
print(random.random())
print(random.random())
random.seed(2)
print(random.random())
print(random.random())
random.seed(1)
print(random.random())
print(random.random())

# Compound Assignment
# incremented: x += 1 is equal to x = x + 1
# decremented: x -= 1 is equal to x = x - 1
# multiply and assign x *= 2 is equal to x = x * 2

# Chicago
# see 42chicago.py

