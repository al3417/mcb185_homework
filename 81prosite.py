import mcb185
import sys
import re

# find the seq matches the prosite pattern
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	if 'DKTGT' in seq: print(defline)

# a patter plus a string
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	if re.search('DKTGT', seq): print(defline)

# use [] for any of them
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	if re.search('DKTGT[LIVM][TI]', seq): print(defline)

# x(2,4) means 2 to 4 aa; (3) means exactly 3
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	if re.search('C.{2,4}C.{3}[LIVMFYWC].{8}H.{3,5}H', seq): 
		print(defline)

# can also extract text
pat = '(C.{2,4}C.{3}[LIVMFYWC].{8}H.{3,5}H)' #each () is a match group
for defline, seq in mcb185.read_fasta(sys.argv[1]):
		m = re.search(pat, seq)
		if m: print(m.group(1))
