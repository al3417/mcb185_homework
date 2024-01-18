import math

def quadratic(a,b,c):

    dis = b**2 - (4*a*c)

    if dis == 0:
        result1 = (-b)/(2*a)
        return result1

    elif dis > 0:
        result1 = ((-b)+math.sqrt(b**2-4*a*c))/(2*a)
        result2 =((-b)-math.sqrt(b**2-4*a*c))/(2*a)
        return result1,result2

    else: 
        return 'No Real Solution'
    

# 4x^2 + 2x + 5
print(quadratic(4,2,5))     # No Real Solution

# x^2 - 2x + 1
print(quadratic(1,-2,1))    # x=1

# x^2 - 8x + 5
print(quadratic(1,-8,5))    # x1=7.31662 x2=0.68337


