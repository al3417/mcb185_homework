seq = 'ACGT'

print('  ', end=' ')
for nt in seq:
	print(nt, end='  ')
print()

for i in seq:
	print(i, end=' ')
	for j in seq:
		if i == j:	
			print('+1', end=' ')
		else:
			print('-1', end=' ')
	print()
		
