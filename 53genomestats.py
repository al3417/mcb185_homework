import gzip
import sys

def minimum(vals):
	mini = vals[0]
	for val in vals[1:]:
		if val < mini: mini = val
	return mini

def maximum(vals):
	maxi = vals[0]
	for val in vals[1:]:
		if val > maxi: maxi = val
	return maxi

def mean(vals):
	total = 0
	for val in vals:
		total += val
	return total / len(vals)

def std(vals, mean):
	variance = 0
	for val in vals:
		variance += (val - mean) ** 2
	return (variance / len(vals)) ** 0.5

def median(vals):
	vals.sort()
	n = len(vals)
	middle = n // 2
	if n % 2 ==0:	return (vals[middle - 1] + vals[middle]) / 2
	else:			return vals[middle]

gffpath = sys.argv[1]
feature = sys.argv[2]
length = []

with gzip.open(gffpath, 'rt') as gff:
	for line in gff:
		if	line[0] == '#': continue
		words = line.split()
		if words[2] != feature: continue
		beg = int(words[3])
		end = int(words[4])
		length.append(end - beg +1)

count =len(length)
maxi_length		= maximum(length)
mini_length		= minimum(length)
mean_length		= mean(length)
std_length		= std(length, mean_length)
median_length	= median(length)
print(count, mini_length, maxi_length, mean_length, std_length, median_length)
