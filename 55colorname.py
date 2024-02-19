import sys

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])

def dtc(P, Q):
	d = 0
	for p, q in zip(P, Q):
		d += abs(p - q)
	return d

def find_color(file, R, G, B):
	closest_color = None
	min_distance = 100000000

	with open(file, 'rt') as file:
		for line in file:
			words = line.split('\t')
			color_name = words[0]
			rgb = words[2]
			r, g, b = rgb.split(',')
			r, g, b = int(r), int(g), int(b)
			
			distance = dtc((R, G, B), (r, g, b))
			if distance < min_distance:
				min_distance = distance
				closest_color = color_name
	return closest_color

color = find_color(colorfile, R, G, B)
print(color)
