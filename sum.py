
def chksum(s):
	c = 0
	for i in s:
		c = c + ord(i)
	return c % 256
	
def maxchar(s):
	mx = 0
	for i in s:
		if ord(i) > mx:
			mx = ord(i)
	return mx

def minchar(s):
	mn = 256
	for i in s:
		if ord(i) < mn:
			mn = ord(i)
	return mn

import math

def euler(limit):
	e = 0
	for n in range(limit):
		e = e + 1 /  math.factorial(n)
		print(e)
	return e

name = 'natalia'
print(chksum(name))
print(maxchar(name))
print(minchar(name))
print(euler(20))


