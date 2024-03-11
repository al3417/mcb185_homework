import sys
import dogma
import mcb185
import gzip

fasta = sys.argv[1]
min_length = int(sys.argv[2])

def generate_frames(seq):
	frames = []
	# Forward
	frames.append(seq)
	frames.append(seq[1:])	# skip 1nt
	frames.append(seq[2:])	# skip 2nt

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

def find_orfs(seq, min_length):
	orfs = []
	frames = generate_frames(seq)
	aa_frames = translate_frames(frames)

	index = 0
	for aa_seq in aa_frames:
		frame_offset = index % 3 # 0, 1, 2
		if index < 3:
			strand = '+'
		else:
			strand = '-'
		i = 0

		while i < len(aa_seq):
			if aa_seq[i] == 'M':
				end_pos = aa_seq[i:].find('*')  # find * after M and new value for end
				if end_pos != -1:
					start_nt = (i * 3) + frame_offset
					end_nt = (i + end_pos) * 3 + frame_offset

					if (end_nt - start_nt + 1) >= min_length:
						orf_table = {
							'start': start_nt,
							'end': end_nt,
							'strand': strand,
						}
						orfs.append(orf_table)	# list of paired value

					i += end_pos + 1  # move i after *
				else:
					break  
			else:
				i += 1

		index += 1  

	return orfs

# I use the GFF feature from wikipedia
def genefinder(fasta, min_length):
	for name, seq in mcb185.read_fasta(fasta):
		orfs = find_orfs(seq, min_length)
		i = 1
		for orf in orfs:	# each paired value
			start = orf['start']
			end = orf['end']
			strand = orf['strand']
			gff_line = f"{name}\tgenefinder\tCDS\t{start+1}\t{end+1}\t.\t{strand}\t0\tID={i}"
			print(gff_line)
			i += 1

genefinder(fasta, min_length)

