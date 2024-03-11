import gzip
import sys
import math
import mcb185

def find_entropy(seq):
# A, C, G, T
	counts = [0, 0, 0, 0]
	total_nt = 0
	entropy = 0

	for nt in seq:
		if nt == 'A'	: counts[0] += 1
		elif nt == 'C'	: counts[1] += 1
		elif nt == 'G'	: counts[2] += 1
		elif nt == 'T'	: counts[3] += 1
		total_nt += 1

	for count in counts:
		if count > 0:
			probability = count / total_nt
			entropy = entropy - (probability * math.log2(probability))
	return entropy

fasta = sys.argv[1]
window_size = int(sys.argv[2])
entropy_threshold = float(sys.argv[3])

def mask(fasta, window_size, entropy_threshold):
	for name, seq in mcb185.read_fasta(fasta):
		print(f'>{name}')
		individual_nts = list(seq)

		for i in range(0, len(seq) - window_size + 1):
			window = seq[i:i+window_size]
			if find_entropy(window) < entropy_threshold: 
				for nt in range(i, i + (window_size)): 
					individual_nts[nt] = 'N'
		
		masked_seq = ''.join(individual_nts)
		for i in range(0, len(masked_seq), 60):
			print(masked_seq[i:i+60])

mask(fasta, window_size, entropy_threshold)

	
