# A simple CLI

import argparse
import gzip
import sys
import math
import mcb185

'''
parser = argparse.ArgumentParser(description='DNA entropy filter')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('size', type=int, help='window size')
parser.add_argument('entropy', type=float, help='entropy threshold')
arg = parser.parse_args()
print('dusting with', arg.file, arg.size, arg.entropy)
'''
'''
parser = argparse.ArgumentParser(description='DNA entropy filter')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('--size', type=int, default=20,
	help='window size [%(default)i]')
parser.add_argument('--entropy', type=float, default=1.4,
	help='entropy threshold [%(default).3f]')

arg = parser.parse_args()
print('dusting with', arg.file, arg.size, arg.entropy)
'''

'''
# Flags
# turns on/off some behavior 
parser = argparse.ArgumentParser(description='DNA entropy filter')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('--size', type=int, default=20,
	help='window size [%(default)i]')
parser.add_argument('--entropy', type=float, default=1.4,
	help='entropy threshold [%(default).3f]')
parser.add_argument('--lower', action='store_true', help='soft mask')
arg = parser.parse_args()
print('dusting with', arg.file, arg.size, arg.entropy, arg.lower)
'''

# Short and Long
# ability to use both short (-s,-e) and long (--size,--entropy) argument
#!/usr/binenv python3
import argparse
import math
import mcb185

parser = argparse.ArgumentParser(description='DNA entropy filter')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('-s', '--size', type=int, default=20,
	help='window size [%(default)i]')
parser.add_argument('-e', '--entropy', type=float, default=1.4,
	help='entropy threshold [%(default).3f]')
parser.add_argument('--lower', action='store_true', help='soft mask')
arg = parser.parse_args()
print('dusting with', arg.file, arg.size, arg.entropy, arg.lower)

fasta = arg.file
window_size = arg.size
entropy_threshold = arg.entropy
upper_to_lower = {'A': 'a', 'C': 'c', 'G': 'g', 'T': 't'}

def find_entropy(seq):
	# A, C, G, T
	counts = [0, 0, 0, 0]
	total_nt = 0
	entropy = 0

	for nt in seq:
		if nt == 'A': counts[0] += 1
		elif nt == 'C': counts[1] += 1
		elif nt == 'G': counts[2] += 1
		elif nt == 'T': counts[3] += 1
		total_nt += 1

	for count in counts:
		if count > 0:
			probability = count / total_nt
			entropy = entropy - (probability * math.log2(probability))
	return entropy

def mask(fasta, window_size, entropy_threshold):
	for name, seq in mcb185.read_fasta(fasta):
		print(f'>{name}')
		individual_nts = list(seq)
		for i in range(0, len(seq) - window_size + 1):
			window = seq[i:i+window_size]
			current_entropy = find_entropy(window)
			
			if current_entropy < entropy_threshold:
				for nt_index in range(i, i + window_size):
					nt = seq[nt_index]
					if nt in upper_to_lower:
						lower_nt = upper_to_lower[nt]
						individual_nts[nt_index] = lower_nt 

		masked_seq = ''.join(individual_nts) 
		for i in range(0, len(masked_seq), 60):
			print(masked_seq[i:i+60])

mask(fasta, window_size, entropy_threshold)

