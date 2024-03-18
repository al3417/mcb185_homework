import argparse
import mcb185
import dogma
import gzip

parser = argparse.ArgumentParser(description='mRNA translator.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('-m', '--min', type=int, default=100, 
	help='minimum protein length [100]')
parser.add_argument('-a', '--anti', action='store_true', 
	help='also examine anti-parallel strand')
arg = parser.parse_args()

print('translating:', arg.file, arg.min, arg.anti)

def slice_protein(aa_frames):
	all_proteins = []

	for aa_seq in aa_frames:
		i = 0
		while i < len(aa_seq):
			if aa_seq[i] == 'M':
				end_pos = aa_seq[i:].find('*')  # find * after M and new value for end

				if end_pos != -1:
					end_pos += i
					protein = aa_seq[i:end_pos]  
					all_proteins.append(protein)
					i = end_pos + 1  # move i after *
				else:
					break
			else:
				i += 1

	return all_proteins

def find_proteins(proteins, min_length):
	long_enough_proteins = []
	for protein in proteins:
		if len(protein) >= min_length:
			long_enough_proteins.append(protein)
	return long_enough_proteins

def tln():
	for name, seq in mcb185.read_fasta(arg.file):
		translated_seq = dogma.translate(seq)
		proteins = slice_protein([translated_seq])
		if arg.anti == True:
			anti_translated_seq = translate(mcb185.anti_seq(seq))
			proteins += slice_protein([anti_translated_seq])
		long_proteins = find_proteins(proteins, arg.min)
		for protein in long_proteins:
			print(f'>{name}')
			print(protein)

tln()

