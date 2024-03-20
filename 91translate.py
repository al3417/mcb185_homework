import argparse
import mcb185
import dogma
import gzip

parser = argparse.ArgumentParser(description='mRNA translator')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('-m', '--min', type=int, default=100, 
	help='minimum protein length [100]')
parser.add_argument('-a', '--anti', action='store_true', 
	help='also examine anti-parallel strand')
arg = parser.parse_args()

print('translating:', arg.file, arg.min, arg.anti)

file_name = arg.file
min_length = arg.min
check_anti = arg.anti


def find_orf(seq):
	start_codon = 'ATG'
	stop_codons = {'TAA', 'TAG', 'TGA'}
	orf = ''
	
	start_index = seq.find(start_codon)
	if start_index != -1:
		truc_seq = seq[start_index:]

		for i in range(0, len(truc_seq), 3):
			codon = truc_seq[i:i+3]
			if codon in stop_codons:
				orf = truc_seq[:i+3]
				break
	
	return orf

def process_sequences(file_name, min_length, check_anti):

	for name, sequence in mcb185.read_fasta(file_name):
		orf = find_orf(sequence)
		protein = dogma.translate(orf)
		if len(protein) >= min_length:
			print(f'>{name}')
			for i in range(0, len(protein), 60):
				print(protein[i:i+60].rstrip('*'))

		if check_anti == True:
			anti_seq = mcb185.anti_seq(sequence)
			anti_orf = find_orf(anti_seq)
			anti_protein = dogma.translate(anti_orf)
			if len(anti_protein) >= min_length:
				print(f'>{name}')
				for i in range(0, len(anti_protein), 60):
					print(anti_protein[i:i+60].rstrip('*'))

process_sequences(file_name, min_length, check_anti)

