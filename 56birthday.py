import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

def birthday(trials, days, people):
	count = 0

	for  n in range(trials):
		birthdays = []
		for i in range(people):
			bday = random.randint(0, days - 1)
			birthdays.append(bday)
		birthdays.sort()

		for i in range(1, len(birthdays)):
			if birthdays[i] == birthdays[i - 1]:
				count += 1
				break

	probability = (count / trials) * 100
	return probability

print(birthday(trials, days, people))



