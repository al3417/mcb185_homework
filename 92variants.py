import argparse
import gzip

parser = argparse.ArgumentParser(description='variant reporter')
parser.add_argument('gff', type=str, 
	help='GFF file')
parser.add_argument('vcf', type=str, 
	help='VCF file')
arg = parser.parse_args()
print('processing with', arg.gff, arg.vcf)

gff_data = {}

with gzip.open(arg.gff, 'rt') as gff:
	for line in gff:
		parts = line.rstrip().split()
		roman = parts[0]
		feature = parts[2]
		start = int(parts[3])
		end = int(parts[4])

		if roman not in gff_data: gff_data[roman] = []
		gff_data[roman].append({'start': start, 'end': end, 'feature': feature})

with gzip.open(arg.vcf, 'rt') as vcf:
	for line in vcf:
		if not line.startswith('#'):
			parts = line.rstrip().split()
			roman_vcf = parts[0]
			position = int(parts[1])

			features = {}
			has_feature = False

			for gff_entry in gff_data[roman_vcf]:
				if gff_entry['start'] <= position <= gff_entry['end']:
					current_feature = gff_entry['feature']
					if current_feature not in features:
						features[current_feature] = True
						has_feature = True

			feature_list = ','.join(features.keys())
			if has_feature == True:
				print(f'{roman_vcf}\t{position}\t{feature_list}')
