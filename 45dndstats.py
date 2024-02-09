import random

# 3D6
tot_rolls = 10000

def dnd_3d6():
	tot_score = 0
	for i in range(tot_rolls):
		tot_score += random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
	avg = tot_score / tot_rolls
	return avg

# 3D6r1
tot_rolls = 10000

def dnd_3d6r1():
	tot_score = 0

	for i in range(tot_rolls):
		roll_score = 0
		for n in range(3):
			ind_roll = random.randint(1, 6)
			if ind_roll == 1: ind_roll = random.randint(1, 6)
			roll_score += ind_roll
		tot_score += roll_score

	avg = tot_score / tot_rolls
	return avg

#3D6x2
tot_rolls = 10000

def dnd_3d6x2():
	tot_score = 0
	
	for i in range(tot_rolls):
		roll_score = 0
	
		for n in range(3):
			d1 = random.randint(1, 6)
			d2 = random.randint(1, 6)
			if d1 > d2:
				roll_score += d1
			else:
				roll_score += d2
		tot_score += roll_score

	avg = tot_score / tot_rolls
	return avg

# 4D6d1
tot_rolls = 10000

def dnd_4d6d1():
	tot_score = 0

	for i in range(tot_rolls):
		roll_sum = 0
		min_roll = 7
		
		for i in range(4):
			roll =  random.randint(1, 6)
			roll_sum += roll
			if roll < min_roll:
				min_roll = roll
		roll_score = roll_sum - min_roll
		tot_score += roll_score

	avg = tot_score / tot_rolls
	return avg

print(dnd_3d6())
print(dnd_3d6r1())
print(dnd_3d6x2())
print(dnd_4d6d1())
