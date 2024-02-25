# skew = (G - C) / (G + C)
# if G is leaving the window, GC -1 and G -1
# if C is leaving the window, GC -1 and C -1
# if G enters the window, GC +1 and G +1
# if C enters the window, GC +1 and C +1

# I ran the fna.gz file
# 62skewer: 17.278s for w=1000, 18.58s for w=3000, 19.163s for w=9000
# 61skewer: 32.91s for w=1000, 54.87s for w=3000

import mcb185
import sys
import dogma

w = 1000

for name, seq in mcb185.read_fasta(sys.argv[1]):
	g_count = seq[:w].count('G')
	c_count = seq[:w].count('C')
	gc_count = g_count + c_count
	gc_composition = gc_count / w
	gc_skew = (g_count - c_count) / gc_count

	for i in range(1, len(seq) - w + 1):
		out_nt = seq[i - 1]
		if out_nt == 'G':
			gc_count	-= 1
			g_count 	-= 1
		elif out_nt == 'C':
			gc_count	-= 1
			c_count		-= 1

		in_nt = seq[i + w - 1]
		if in_nt == 'G':
			gc_count	+= 1
			g_count		+= 1
		elif in_nt == 'C':
			gc_count	+= 1
			c_count		+= 1
	
		gc_composition	= gc_count / w
		gc_skew			= (g_count - c_count) / gc_count
		print(f'{i}\t{gc_composition:.3f}\t{gc_skew:.3f}')
		

