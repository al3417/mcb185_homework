import sys
import dogma
import mcb185
import gzip

fasta = sys.argv[1]
min_length = int(sys.argv[2])

'''
FIrst: using the original nucleotide sequence to generate a reverse nt seq 

Second: 
generate three frame for each nt sequence
for the first frame: 
keep everything the same
for the second frame: 
delete the first nucleotide or start reading from the second nt
for the third frame: 
delete the first two nt or starting reading from the third nt

Third:
After have six nucleotide strand, 
three frame for forward and three frame for reverse. 
Translate all six nt strands seperately into six aa strands.

Fourth:
Check each strands seperately. read along the strand, 
splice out all sequences using 'M' as start position,
 '*' (stop) as stop position. 
Generate all spliced sequences for each strands

Fifth:
Check everything in each list, select those with length >= 100

Sixth:
The output

'''
#I think I over complicate the solution. 
#I was keep getting 6050 and it took me a long time to fix it.

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

'''
test_frame1 = generate_frames('ATGAAATTTGGGTGA')
test_frame2 = generate_frames('ATGAAATTTGGGCCTGA') # not %3
test_frame3 = generate_frames('ATGAAATTTGGGCCAAATTTTTTAAATTGA') 
print(test_frame1)
print(test_frame2)
print(test_frame3)
'''

def translate_frames(frames):
	aa_frames = []
	for frame in frames:
		aa_frames.append(dogma.translate(frame))
	return aa_frames

'''
translated_test_frame1 = translate_frames(test_frame1)
translated_test_frame2 = translate_frames(test_frame2)
translated_test_frame3 = translate_frames(test_frame3)
print(translated_test_frame1)
print(translated_test_frame2)
print(translated_test_frame3)
'''

def slice_protein(aa_frames):
	all_proteins = []

	for aa_seq in aa_frames:
		i = 0
		while i < len(aa_seq):
			if aa_seq[i] == 'M':
				end_pos = aa_seq[i:].find('*')  # find * after M and new value for end

				if end_pos != -1:
					end_pos += i
					protein = aa_seq[i:end_pos]  # M to before *
					all_proteins.append(protein)
					i = end_pos + 1  # move i after *
				else:
					break
			else:
				i += 1

	return all_proteins

'''
sliced_proteins1 = slice_protein(translated_test_frame1)
sliced_proteins2 = slice_protein(translated_test_frame2)
sliced_proteins3 = slice_protein(translated_test_frame3)

print(sliced_proteins1)
print(sliced_proteins2)
print(sliced_proteins3)
'''

def find_proteins(proteins, min_length):
	long_enough_proteins = []
	for protein in proteins:
		if len(protein) >= min_length:
			long_enough_proteins.append(protein)
	return long_enough_proteins

'''
long_enough1 = find_proteins(sliced_proteins1, 4)
long_enough2 = find_proteins(sliced_proteins2, 4)
long_enough3 = find_proteins(sliced_proteins3, 4)
print(long_enough1)
print(long_enough2)
print(long_enough3)
'''

def profinder(fasta, min_length):
	for name, seq in mcb185.read_fasta(fasta):
		words = name.split()
		first_word = words[0]

		frames = generate_frames(seq)
		aa_frames = translate_frames(frames)
		sliced_proteins = slice_protein(aa_frames)
		long_enough_proteins = find_proteins(sliced_proteins, min_length)

		for i, protein in enumerate(long_enough_proteins):
			defline = f'>{first_word}-prot-{i+1}'
			print(f'{defline}\n{protein}')

profinder(fasta, min_length)


