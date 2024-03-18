import mcb185
import sys
import gzip

def load_seq(file_path):
	sequences = {}
	for name, seq in mcb185.read_fasta(file_path):
		roman = name.split()[0]
		sequences[roman] = seq
	return sequences

def process_gff_file(file_path, sequences):
	plus_introns = []
	minus_introns = []

	with gzip.open(file_path, 'rt') as file:
		for line in file:
			parts = line.rstrip().split()
			if 'RNASeq_splice' in parts:
				seqid = parts[0]
				if seqid in sequences:
					intron_dict = {
						'seqid': seqid,
						'source': parts[1],
						'type': parts[2],
						'start': int(parts[3]),
						'end': int(parts[4]),
						'score': parts[5],
						'strand': parts[6],
						'phase': parts[7],
						'attributes': parts[8]
					}

					if intron_dict['strand'] == '+':
						plus_introns.append(intron_dict)
					elif intron_dict['strand'] == '-':
						minus_introns.append(intron_dict)

	for intron in minus_introns:
		temp = intron['start']
		intron['start'] = intron['end']
		intron['end'] = temp

	return plus_introns, minus_introns

def extract_sites(introns, sequences):
	d_plus = []
	a_plus = []
	d_minus = []
	a_minus = []

	for intron in introns:
		seqid = intron['seqid']
		sequence = sequences[seqid]
		start = intron['start']
		end = intron['end']

		if intron['strand'] == '+':
			donor_site = sequence[start - 1:start + 5]
			acceptor_site = sequence[end - 7:end]
			d_plus.append(donor_site)
			a_plus.append(acceptor_site)
		elif intron['strand'] == '-':
			donor_site = mcb185.anti_seq(sequence[start - 6:start])
			acceptor_site = mcb185.anti_seq(sequence[end - 1:end + 6])
			d_minus.append(donor_site)
			a_minus.append(acceptor_site)

	return d_plus, a_plus, d_minus, a_minus

def pwm_donors(d_plus, d_minus):
	pwm = {
		'A': [0, 0, 0, 0, 0, 0],
		'C': [0, 0, 0, 0, 0, 0],
		'G': [0, 0, 0, 0, 0, 0],
		'T': [0, 0, 0, 0, 0, 0]
	}
	for site in d_plus:
		for i, nt in enumerate(site):
			position_counts = pwm[nt]
			position_counts[i] += 1

	for site in d_minus:
		for i, nt in enumerate(site):
			position_counts = pwm[nt]
			position_counts[i] += 1

	print('AC DEMO1\nXX\nID DON\nXX\nDE splice donor')
	print('PO      A       C       G       T')

	A = pwm['A']
	C = pwm['C']
	G = pwm['G']
	T = pwm['T']

	for i in range(6):
		print(f'{i+1:<8}{A[i]:<8}{C[i]:<8}{G[i]:<8}{T[i]:<8}')
	print('XX\n//\n')

def pwm_acceptors(a_plus, a_minus):
	pwm = {
		'A': [0, 0, 0, 0, 0, 0, 0],
		'C': [0, 0, 0, 0, 0, 0, 0],
		'G': [0, 0, 0, 0, 0, 0, 0],
		'T': [0, 0, 0, 0, 0, 0, 0]
	}
	for site in a_plus:
		for i, nt in enumerate(site):
			position_counts = pwm[nt]
			position_counts[i] += 1

	for site in a_minus:
		for i, nt in enumerate(site):
			position_counts = pwm[nt]
			position_counts[i] += 1

	print('AC DEMO1\nXX\nID DON\nXX\nDE splice acceptor')
	print('PO      A       C       G       T')

	A = pwm['A']
	C = pwm['C']
	G = pwm['G']
	T = pwm['T']

	for i in range(7):
		print(f'{i+1:<8}{A[i]:<8}{C[i]:<8}{G[i]:<8}{T[i]:<8}')
	print('XX\n//\n')

filepath = '/home/zhe/Code/MCB185/data/C.elegans.fa.gz'
seq = load_seq(filepath)

gff_file = '/home/zhe/Code/MCB185/data/C.elegans.gff.gz'
plus_introns, minus_introns = process_gff_file(gff_file, seq)

extracted_sites = extract_sites(plus_introns + minus_introns, seq)

d_plus = extracted_sites[0]
a_plus = extracted_sites[1]
d_minus = extracted_sites[2]
a_minus = extracted_sites[3]

pwm_donors(d_plus, d_minus)
pwm_acceptors(a_plus, a_minus)

