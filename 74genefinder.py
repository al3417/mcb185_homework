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

def genefinder(fasta, min_length):
	for name, seq in mcb185.read_fasta(fasta):
		frames = generate_frames(seq)
		aa_frames = translate_frames(frames)

		index = 0
		i = 1
		for aa_seq in aa_frames:
			frame_offset = index % 3
			if index < 3:
				strand = '+'
			else:
				strand = '-'

			pos = 0
			while pos < len(aa_seq):
				if aa_seq[pos] == 'M':
					end_pos = aa_seq[pos:].find('*')  # find * after M
					if end_pos != -1:
						start = (pos * 3) + frame_offset
						end = (pos + end_pos) * 3 + frame_offset

						if (end - start + 1) >= min_length:
							gff_line = f'{name}\tgenefinder\tCDS\t{start + 1}\t{end + 1}\t.\t{strand}\t0\tID={i}'
							print(gff_line)
							i += 1

						pos += end_pos + 1  # move pos after *
					else:
						break
				else:
					pos += 1

			index += 1

genefinder(fasta, min_length)

