import random
games = 10
for i in range(games):
	print(f'game #{i}')
	for target in range(2, 13):
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		if d1 + d2 == target:
			print(f'yay, rolled {d1} and {d2} for {target} points')

# What is the avg score for a game of Chicago?
# to get an accurate avg score, we need a lots of data
# just get the sum
games = 10	
for i in range(games):
	score = 0	#reset the score for each i
	for target in range(2, 13):
		if random.randint(1, 6) + random.randint(1, 6) == target:
			score += target # score = score + target
	print(score)	#output score before reset the score

# What is the approximate distribution of game scores?
# sorting the output in terminal
# python3 42chicago.py | sort -n | uniq -c | sort -n
# -n is numeric, -r is reverse order, -c used to list lines with occurrences
# if games = 1000000, need to keep the calc internal to python without output, directly sort will take too much memory. make two variable:
# 1--to keep track of the tot points
# 2--to count the numbers of games that end with zero
# use a log to report %
import sys
games = 1000000
log = games // 100 # report progress at 1% intervals
total = 0
zeroes = 0
for i in range(games):
	if 1 % log == 0: print(f'{100 * i/games:.0f}', file=sys.stderr) 
# sys.stderr to see the progress %, f:.to round up the certain digit
	score = 0
	for target in range(2, 13):
		if random.randint(1, 6) + random.randint(1, 6) == target:
			score += target
	if score == 0: zeroes += 1
	total += score
print(total / games)	# avg score of the game
print(zeroes / games)	# % of ending with a score of zero


# How often does a player end a game with a score of zero?

