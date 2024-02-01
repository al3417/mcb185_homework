# while
# 'while' followed by an True or False value

i = 0		# store integer
while True:		# notice T 
	i = i + 1		# each loop +1
	print('hey',i)	# print hey and the value of i
	if i == 3: break	# once i reach 3, loop break


# for i in range()
for i in range(1, 10, 3): # start 1, exlusive 10, increment 3
	print(i)
# to set increment by one, leave the last argument empty
for i in range(0, 5):	 # ( is inclusive, ) is exclusive
	print(i)
# if loop start at 0, skip initial value, put the exlusive ending value
for i in range(5):
	print(i)

# for item in container
# loop over items in a container
for char in 'hello':	# 5 letter in 'hello' string
	print(char)

seq = 'GAATTC'
for nt in seq:
	print(nt)

# Nested Loops
# loop inside loops
for nt1 in 'ACGT':	  # this is outer loop
	for nt2 in 'ACGT':  # this is inner loop
		if nt1 == nt2:  print(nt1, nt2, '+1')   # +1 for a match
		else:		   print(nt1, nt2, '-1')   # -1 for a mismatch
# add a variable nts to holds the alphabet
nts = 'ACGT'			# define nts variable
for nt1 in nts:		 # replace the content with a variable
	for nt2 in nts:
		if nt1 == nt2:  print(nt1, nt2, '+1')   
		else:		   print(nt1, nt2, '-1')  
# unique combination
limit = 4						   # def a variable
for i in range(0, limit):		   # from 0 to 4
	for j in range(i + 1, limit):   # each number from i+1 to 4
		print(i+1, j+1)			 # output i and j value for each loop
print('sp')
# just-combination
limit = 4							  
for i in range(0, limit):		 
	for j in range(i, limit):	   # no difference between the range of loop
		print(i+1, j+1)			 

# Algorithms
# calculate GC composition of a nt seq
def gc_comp(seq):
	gc_count = 0	# create variable to store value in loop
	total = 0
	for nt in seq:  # for each nt inside the seq...
		if nt == 'C' or nt == 'G':  
			gc_count = gc_count + 1 # for every nt count, add 1 if g or c
		total = total + 1		   # for every nt count, add 1 to total count
	return gc_count/total

print(gc_comp('ACAGCGAAT'))


# Practice
# triangular number
def findtn(num):
	tri_num = 0 # need to def inside func, won't work if def outside
	for i in range(1, num + 1):
		tri_num = tri_num + i
	return tri_num
num = 9
print(findtn(num))

# factorial of a number
def findfc(num):
	if num == 0: return 1
	fc_num = 1	  # cannot start at zero, or will always get zero
	for i in range(1, num + 1):
		fc_num = fc_num*i
	return fc_num
num = 3
print(findfc(num))

# estimate Euler's number

# determine if a number is a perfect square
import math

def ispsq(num):
	assert num > 0
	result1 = num - math.sqrt(num) 
	if result1-math.floor(result1) == 0:
		return 'the number is a perfect square'
	else: return 'the number is NOT a perfect square'

print(ispsq(25))
# or
def is_perfect_square(n):
	root = math.sqrt(n)
	if math.isclose(root, root // 1): return True
	else: return False

# determine if a number is prime
def is_prime(n):
	for den in range(2, n//2):
		if n % den == 0: return False
	return True

