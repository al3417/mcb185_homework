import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

def birthday(trials, days, people):
	count = 0

	for trial in range(trials):
		cal = []
		for i in range(days):
			cal.append(0)

		for i in range(people):
			d = random.randint(0, days - 1)
			cal[d] += 1

			if cal[d] >= 2:
				count += 1
				break

	probability = (count / trials) * 100
	return probability

print(birthday(trials, days, people))

