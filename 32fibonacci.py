def fibo(n):
	a = 0
	b = 1
	for i in range(n):
		print(a, end=',')
		c = a	# the order of events matters
		a = b
		b = c + b

fibo(10)
