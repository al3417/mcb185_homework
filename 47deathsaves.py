import random

def death_save():
	roll = random.randint(1, 20)
			
	if roll == 1:
		return 'extra fail count'
	elif roll == 20:
		return 'revive count'
	elif roll >= 10:
		return 'success count'
	else:
		return 'fail count'

times = 100000
def death_prob():
	death = 0
	stable = 0
	revived = 0

	for i in range(times):
		failure = 0
		success = 0
	
		while failure < 3 and success < 3:
			result = death_save()
			if result == 'extra fail count':
				failure += 2
			elif result == 'success count':
				success += 1
			elif result == 'fail count':
				failure += 1
			elif result == 'revive count':
				revived += 1
				break

		if failure >= 3: 
				death += 1
		elif success >= 3:
				stable += 1
	

	death_prob = death / times
	stable_prob = stable /times
	revived_prob = revived / times
	return death_prob, stable_prob, revived_prob

print(death_prob())
			


		
	
