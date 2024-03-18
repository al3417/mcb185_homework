'''
I use 14nt; pos 10,11,13, is the start codon.

1. extract the position of CDS

2. use the start and end position to locate the actual nucleotide sequence
for normal gene: the starting position is the first number.
extract 9 nt before the start_pos, start_pos, and 4 nt after the start_pos

for complementary gene: the starting position is the second number.
extract 4 nt before the start_pos, start_pos, and 9 nt after start_pos

3. use antiseq to find the actual sequence of complementary gene

4. return all the 14nts sequences
5. do a count for each position
'''
import gzip
import mcb185
import sys

def	extract_seq(line):
	seq_list = []	
	nt_dict = {'a': 'A', 'c': 'C', 'g': 'G', 't': 'T'}

	for	nt in line:
		if nt in nt_dict:
			seq_list.append(nt_dict[nt])
	
	return seq_list

def	locate_seq(gene_positions, sequence):
	for	gene in gene_positions:
		if 'normal_start' in gene:
			start_pos = gene['normal_start'] - 10
			if start_pos < 0:
				start_pos = 0
			end_pos = gene['normal_start'] + 4
			gene['sequence'] = sequence[start_pos: end_pos]
		
		else:
			comp_start_pos = gene['comp_start'] - 5
			if comp_start_pos < 0:
				comp_start_pos = 0
			
			comp_end_pos = gene['comp_start'] + 9
			extracted_sequence = sequence[comp_start_pos: comp_end_pos]
			gene['sequence'] = mcb185.anti_seq(extracted_sequence)

def	count_nts(gene_positions):
	count_dict = {
		'A': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		'C': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		'G': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		'T': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	}
	for	gene in gene_positions:
		if 'sequence' in gene:
			sequence = gene['sequence']
			for	i, nt in enumerate(sequence):
				if i < 14:
					position_counts = count_dict[nt]
					position_counts[i] += 1

	return count_dict

def	gbff_file(filepath):
	gene_positions = []
	sequence_parts = []
	data_section = False

	with gzip.open(filepath, 'rt') as fp:
		for line in fp:
			line = line.rstrip()

			if line.startswith('     gene'):
				if 'complement' in line:
					c_info_start = line.find('(') + 1
					c_info_end = line[c_info_start:].find(')') + c_info_start
					c_info = line[c_info_start:c_info_end]
					positions = c_info.split('..')

					if len(positions) == 2:
						start_pos = int(positions[1])
						end_pos = int(positions[0])

						gene_positions.append({
							'comp_start': start_pos,
							'end_pos': end_pos,
							'strand': 'complementary'
						})
				else:
					n_info_start = line.find('gene') + 4
					n_info = line[n_info_start:].rstrip()
					positions = n_info.split('..')

					if len(positions) == 2:
						start_pos = int(positions[0])
						end_pos = int(positions[1])

						gene_positions.append({
							'normal_start': start_pos,
							'end_pos': end_pos,
							'strand': 'normal'
						})

			if line.startswith('ORIGIN') or data_section == True:
				if line.startswith('//'):
					data_section = False
				else:
					for seq_part in extract_seq(line):
						sequence_parts.append(seq_part)
					data_section = True

	sequence = ''.join(sequence_parts)
	locate_seq(gene_positions, sequence)
	nt_counts = count_nts(gene_positions)

	print('AC IMTSU001')
	print('XX')
	print('ID ECKOZ')
	print('XX')
	print('DE I made this shit up')
	print('PO      A       C       G       T')

	for i in range(14):
		a_count = nt_counts['A'][i]
		c_count = nt_counts['C'][i]
		g_count = nt_counts['G'][i]
		t_count = nt_counts['T'][i]
		print(f'{i+1:<8}{a_count:<8}{c_count:<8}{g_count:<8}{t_count:<8}')

gbff_file(sys.argv[1])


