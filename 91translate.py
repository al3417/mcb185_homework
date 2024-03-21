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

def generate_frames(seq):
	frames = []
	# Forward
	frames.append(seq)
	frames.append(seq[1:])  # skip 1nt
	frames.append(seq[2:])  # skip 2nt

	# Reverse
	reverse_seq = dogma.revcomp(seq)
	frames.append(reverse_seq)
	frames.append(reverse_seq[1:]) 
	frames.append(reverse_seq[2:])

	return frames

def translate_frames(frames):
	aa_frames = []
	for frame in frames:
		aa_frames.append(dogma.translate(frame))
	return aa_frames

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

'''
def check_all_aa_length_100(aa_frames):
	all_meet_length_req = True

	for aa_seq in aa_frames:
		if len(aa_seq) < 100:
			
			all_meet_length_req = False
			break

	if all_meet_length_req == True:
		print('All aa meet length req')
	else:
		print('Not meet')
'''

def process_sequences(file_name, min_length, check_anti):
	for name, seq in mcb185.read_fasta(file_name):

		frames = generate_frames(seq)
		if check_anti == False:
			frames = frames[:3]

		aa_frames = translate_frames(frames)
		
		# check_all_aa_length_100(aa_frames)

		sliced_proteins = slice_protein(aa_frames)
		long_enough_proteins = find_proteins(sliced_proteins, min_length)

		longest_protein = ''
		longest_found = False
		for protein in long_enough_proteins:
			if len(protein) > len(longest_protein):
				longest_protein = protein
				longest_found = True

		if longest_found == True:
			print(f'>{name}')
			for i in range(0, len(protein), 60):
				print(longest_protein[i:i+60].rstrip('*'))

process_sequences(file_name, min_length, check_anti)


