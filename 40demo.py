import random

# produce a number that is 0 <= x < 1
for i in range(5):
	print(random.random())

# choose from the container
for i in range(50):
    print(random.choice('ACGT'), end='')
print()
