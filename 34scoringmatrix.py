seq = 'ACGT'

print('   A  C  G  T')
for i in seq:
	print(i, end=' ')
	for j in seq:
		if i == j:	
			print('+1', end=' ')
		else:
			print('-1', end=' ')
	print()
		
