import math

def findTm(a,c,g,t):
    if a+c+g+t <= 13:
        Tm = (a+t)*2 + (g+c)*4
        return Tm
    else:
        Tm = 64.9 + 41*(g + c -16.4) / (a+t+g+c)
        return Tm

print('The melting temperature of AACCGGTT is :' + str(findTm(2,2,2,2)))            # 24

print('The melting temperature of AACCCCGGTTTTTTTT is :' + str(findTm(2,4,2,8)))    # 38.25




