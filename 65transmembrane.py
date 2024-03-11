import gzip
import mcb185

aas = 'IVLFCMAGTSWYPHEQDNKR'
kd_vals = [4.5, 4.2, 3.8, 2.8, 2.5, 1.9, 1.8, -0.4, -0.7, 
-0.8, -0.9, -1.3,-1.6, -3.2, -3.5, -3.5, -3.5, -3.5, -3.9, -4.5]

def calc_hydro(seq, w, min_kd):
	max_kd = -100000
	for i in range(len(seq) - w + 1):
		pep = seq[i:i + w]
		if 'P' in pep: continue
		kd_sum = 0
		for aa in pep:
			idx = aas.find(aa)
			if idx != -1:
				kd_sum += kd_vals[idx]	
		avg_kd = kd_sum / w
		if avg_kd > max_kd:
			max_kd = avg_kd
	if max_kd >= min_kd:
		return True
	else:
		return False

def is_protein(seq):
	sig_peptide = calc_hydro(seq[:30], 8, 2.5)
	if not sig_peptide:
		return False

	trans_region = calc_hydro(seq[30:], 11, 2.0)
	if not trans_region:
		return False 

	return True



filename = '../MCB185/data/GCF_000005845.2_ASM584v2_protein.faa.gz'
for name, seq in mcb185.read_fasta(filename):
	if is_protein(seq) == True:
		print(name)

