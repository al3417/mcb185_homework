import math

seq = 'GAATTC'
print(seq[0], seq[1])
print(seq[-1])	#count backwards
for nt in seq: print(nt, end='')
print()
for i in range(len(seq)):
	print(i, seq[i])

# Slice
# subset of a container
s =  'ABCDEFGHIJ'
print(s[0:5]) # 0 is initial position, 5 is the end-before limit
print(s[0:8:2]) # increment of two
print(s[:5]) # short cut
print(s[5:])
print(s, s[::], s[::1], s[::-1])

# Tuples
tax = ('Homo', 'sapiens', 9606)
print(tax)
print(tax[0])
print(tax[::-1])	# reverse slice

# enumerate()
nts = 'ACGT'
for i in range(len(nts)):
	print(i, nts[i])
# to use enumerate() with a tuple
for i, nt in enumerate(nts):
	print(i, nt)

# zip()
names = ('adenine', 'cytosin', 'guanine', 'thymine')
for i in range(len(names)):
	print(nts[i], names[i])
# to use zip() to retrieve element from each container
for nt, name in zip(nts, names):
	print(nt, name)
# enumerate the zip
for i, (nt, name) in enumerate(zip(nts, names)):
	print(i, nt, name)

# Lists
nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G'	# you can change the content of list
print(nts)
# use list.append() to add element
nts.append('C')
print(nts)
# remove element from the end of list
last = nts.pop()
print(last)
# sort a mixture of ints and floats
nts.sort()
print(nts)
nts.sort(reverse=True)
print(nts)
# assign another name for the same list
nucleotides = nts
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)
# to make a copy, use list.copy()

#list()
items = list() #create empty list
print(items)
items.append('eggs')
print(items)
stuff = []	#create empty list
stuff.append(3)
print(stuff)
alpha = 'ACDEFGHIKLMPQRSVW'
print(alpha)
aas = list(alpha)
print(aas)

# split() and join()
text = 'good day	to you'
words = text.split()	# split strings into lists of strings
print(words)
line = '1.43, 2.72, 3.14'	# CSV data
print(line.split(','))	# use \t or ,
s = '-'.join(aas)
print(s)
s = ''.join(aas)
print(s)

#Searching
alpha = 'ACDEFGHIKLMPQRSVW'
if 'A' in alpha: print('yes')
if 'a' in alpha: print('no')
print('index G?', alpha.index('G'))
print('find Z?', alpha.find('Z'))
print('find G', alpha.find('G'))
print('find Z', alpha.find('Z'))

# Practice
# return minimum of a list
def min(vals):
	mini = vals[1:]
	for val in vals[1:]:
		if val < mini: mini = val
	return mini

# minmax()
```def minmax(vals):
	mini = vals[0]
	maxi = vals[0]
	for val in vals:
		if val < mini: mini = val
		if val > maxi: maxi =val
return mini, maxi

# mean()

def mean(vals):
	total = 0
	for val in vals: total += val
	return total / len(vals)


# entropy()
#def entropy(probs):
#	h = 0
#	for p in probs:
#		h -= p * math.log2(p)
#	return h
#print(entropy([0,2, 0.3, 0.5]))

# dlk()
#def dkl(P, Q):
#	d = 0
#	for p, q in zip (P, Q):
#		d += p * math.log2(p/q)
#	return d
#p1 = [0.4, 0.3 , 0.2, 0.1]
#p2 = (0.1, 0.3, 0.4, 0.2)
#print(dkl(p1, p2))

# files
#with open(path) as fp:
#	for line in fp:
#		do_something_with(line)

# compressed files
import gzip
# with gzip.open(path, 'rt') s fp:
	for line in fp:
		print(line, end='')

# convert
i = int('42')
x = float('0.61803')

