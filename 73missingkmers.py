import sys
import itertools
import mcb185

file = sys.argv[1]

def missing_kmers(file, limit):
	limit = 8
	k = 1
	found_missing = False

	while found_missing == False and k <= limit:
		count = {}

		for name, seq in mcb185.read_fasta(file):
			for i in range(len(seq) - k + 1):
				kmer = seq[i:i + k]
				rev_kmer = mcb185.anti_seq(kmer)

				if kmer not in count: count[kmer] = 0
				count[kmer] += 1

				if rev_kmer not in count: count[rev_kmer] = 0
				count[rev_kmer] += 1

		missing_kmers = []
		for nts in itertools.product('ACGT', repeat=k):
			kmer = ''.join(nts)
			if kmer not in count:
				missing_kmers.append(kmer)

		if len(missing_kmers) > 0:
			found_missing = True
			print(f"found {len(missing_kmers)} missing kmers:")
			for kmer in missing_kmers:
				print(kmer)
		else:
			k += 1

missing_kmers(file, 8)

