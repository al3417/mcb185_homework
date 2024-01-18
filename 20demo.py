#   20demo.py by Zhe Liu
import math
import sys

print ("hello, again")  # Greeting

print (1.5e-2)
print ("1.5e-2")

print (1+4)
print (5-1)
print (5*1)
print (5/5)
print (5**2)    # exponentiation
print (5//2)    # integar divide
print (5%2)     # remainder
print (5*(2+1))

print(abs(-3))                  # absolute value
print(pow(3,4))                 # 3 to the power of 4
print(round(1.12345,ndigits=3)) # round to 3 digit
print(math.ceil(1.6))           # round up
print(math.floor(1.6))          # round down
print(math.sqrt(9))             # square root
print(math.factorial(6))        # factorial of an integer
print(math.e)                   # print e or pi
 
# compute hypotenuse             
a = 3
b = 4
c = math.sqrt(a**2+b**2)
print(c)

# to see the type of variables
print(type(a), type(b), type(c))    
# a and b is integer and c is floating number

# to change how to sperate variable when printed out
print(type(a), type(b), type(c), sep='---') # changed to '---'

# Functions
def greeting(x):            # use def and : to create a function    
    print('hello ' + x)     # better not have a print inside function

greeting("zhe")

# Example
def pythagoras(a,b):
    c = math.sqrt(a**2 + b**2)
    return c
print(pythagoras(1,1))

# to ensure your function receive correct value, use assert()
def pythagoras(a,b):
    assert(a>0)     # is a bigger than 0?
    assert(b>0)     # is b bigger than 0?
    c = math.sqrt(a**2 + b**2)
    return c
# print(pythagoras(-1,1)) <---- func abort when assertion failed
# or using sys.exit() to write your own error message

#-------------------------Practice--------------------------

# turns negative to positive and vice versa
def neg(i):         # postive to negative
    if i <= 0: sys.exit('error: must input a positive value')
    assert(i>0)
    result = i*(-1)
    return result
print(neg(3))

def pos(i):         # negative to positive
    if i >= 0: sys.exit('error: must input a positive value')
    assert(i<0)    
    result = i*(-1)
    return result
print(pos(-4))


# area, circumferences, volume
def rtarea(a,b):    # area of rectangles
    assert(a>0)
    assert(b>0)
    area = a*b
    return area
print('the area of this rectangle is: ' + str(rtarea(2,4)))  

def ccarea(r):      # area of circle
    assert(r>0)
    area = math.pi * r ** 2
    return area
print('the area of this circle is: ' + str(ccarea(2)))

def tricr(a,b,c):    # circumferences of triangle
    assert(a>0 and b>0 and c>0)
    assert(a**2 + b**2 == c**2)
    cr = a + b + c
    return cr
print('the circumference of the triangle is: ' + str(tricr(3,4,5)))

def sphvol(r):      # volume of a sphere
    assert(r>0)
    vol =  (4/3)*math.pi*(r**3)
    return vol
print('the vol of the sphere is: ' + str(sphvol(3)))


# Convert temp
def ctemp(f):       # from F to C
    result = (f - 32) * (5/9)
    return result
print('Celsius is: ' + str(ctemp(78)))
# want: 78F in Celsius is xxx
# cannot: print(str(f) + 'F in' + 'C is: ' + str(ctemp(78)))



# Convert speed
def mph(kph):       # from kph to mph
    assert (kph>=0)
    result = kph/1.609
    return result
print('The speed is: ' + str(mph(100)))


# DNA concentration from OD260
def conc(dilu,reading):
    assert(dilu>0 and reading>0)
    result = dilu * reading * 50
    return result
print('The concentration at 260nm is: ' + str(conc(2,1.2))+ ' microgram per mililiter')


# Distant b/t two points
def dis(x1,y1,x2,y2):
    dis = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return dis
print ( 'The distance is :' + str(dis(4,5,-1,8)))


# Midpoint b/t two points
def mid(x1,y1,x2,y2):
    midx = (x1+x2)/2
    midy = (y1+y2)/2
    return midx, midy
print(mid(3,4,1,4))


# IF
a = 2
b = 2
if a == b:
    print('a equal b')
print(a,b)

# ELIF
if a < b:
    print('a < b')
elif a > b:
    print('a > b')
else:
    print('a == b')

# Boolean
c = a == b
print(c)
print(type(c))  # this is a True/False types of value

# Chaining
if a < b or a > b:
    print('all things being equal, a and b are not')
if a < b and a > b:
    print('you are living in a strange world')
if not False:
    print(True)

# Warning about floating points
# NEVER expect equality with floating point, set an acceptable parameter to consider equality
a = 0.3
b = 0.1 * 3 # which will give 0.30000000000000004 not 0.3
print(abs(a - b))
if abs(a - b) < 1e-9: print ('close enough')
# or just use math.isclose()
if math.isclose(a,b): print('close enough') 

# String Comparison
s1 = 'A'
s2 = 'B'
s3 = 'a'
if s1 < s2: print ('A < B') # actuallt comparing their ASCII value
if s2 < s3: print('B < a')

# Mismatched Type Error
a = 1
s = 'G'
# if a<s: print('a<s') , int vs str, won't work


#-------------------------Practice-------------------------------

# If a number is an integer
def isinteger(i):
    if i-(math.floor(i)) == 0: print ('The number is a integer.')
    else: print('The number is not a integer.')
isinteger(27.8)
isinteger(14)

# If a number is odd
def isodd(i):
    if i%2 == 0: print ('It is a odd number')
    else: print ('It is NOT a odd number')
isodd(8)

# If a number is a valid probability (?)

# Return molecular weight of DNA letter
def weight(base):
    if type(base) != str: 
        sys.exit('ERROR:please enter a string argument')
    letter = base.upper()
    if letter == 'A': 
        print('The molecular weight of adenine is 313.21 Daltons')
    elif letter == 'T': 
        print('The molecular weight of thymine is 304.2 Daltons')
    elif letter == 'G':
        print('The molecular weight of guanine is 329.21 Daltons')
    else:
        print('The molecular weight of cytosine is 289.18 Daltons')
weight('A')
weight('g')
# weight(a)

# Return the complement of a DNA letter
def comp(base):
    if type(base) != str: 
        sys.exit('ERROR:please enter a string argument')
    letter = base.upper()
    if letter == 'A': print('T')
    elif letter == 'T': print('A')
    elif letter == 'C': print('G')
    else: print('C')
comp('C')



