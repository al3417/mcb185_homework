import gzip
import json

filepath = '/home/zhe/Code/MCB185/data/jaspar2024_core.transfac.gz'

data = []
id = ''
pwm = []
pwm_section = False

with gzip.open(filepath, 'rt') as file:
	for line in file:
		if line.startswith('ID'):
			id = line.split()[1]
		elif line.startswith('PO'):
			pwm_section = True
		elif line.startswith('XX') and pwm_section == True:
			pwm_section = False
			data.append({
				'id': id,
				'pwm': pwm
			})

			id = ''
			pwm = []
		elif pwm_section == True:
			split_line = line.split()
			a = split_line[1]
			c = split_line[2]
			g = split_line[3]
			t = split_line[4]
			pwm.append({'A': a, 'C': c, 'G': g, 'T': t})

print(json.dumps(data, indent=4))

