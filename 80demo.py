# Lists of Things
d = [
		'hello',
		(3.14, 'pi'),
		[-1, 0, 1],
		{'year': 2000, 'month': 7}
]
print(d[0][4], d[1][0], d[2][2], d[3]['month'])

# list of dictionaries
oligo = {
	'Nmae': 'S0116',
	'Length': 18,
	'Sequence': 'ATTTAGGTGACACTATAG',
	'Description': 'SP6 promoter sequencing primer'
}

catalog = []
catalog.append(oligo)

# usuallt read list of records from files
# reading CSV file into a list of records
def read_catalog(filepath):
	catalog = []
	with open(filepath) as fp:
		for line in fp:
			if line.startswith('#'): continue
			name, length, seq, desc = line.rstrip().split(',')
			record = {
				'Name': name,
				'Length': length,
				'Sequence': seq,
				'Description': desc
			}
			catalog.append(record)
	return catalog



catalog = read_catalog('/home/zhe/Code/MCB185/data/primers.csv')
for primer in catalog:
	print(primer['Name'], primer['Description'])

import dogma
import math
for primer in catalog:
	primer['Tm'] = dogma.tm(primer['Sequence'])
print(catalog)

# Dicts of Lists

seq = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGT'
k = 2
kloc = {}
for i in range(len(seq) -k +1):
	kmer = seq[i:i+k]
	if kmer not in kloc: kloc[kmer] = []
	kloc[kmer].append(i)
print(kloc)

# JSON
# use json library to use json.dump() to examine the structure
import json
truc = {
	'animals': {'dog': 'woof', 'cat': 'meow', 'pig': 'oink'},
	'numbers': [1.09, 2.72, 3.14],
	'is_complete': False,
}
print(json.dumps(truc, indent=4))



