import math

def findE(a,c,g,t):
    total = a + c + g + t 
    ap = a/total
    cp = c/total
    gp = g/total
    tp = t/total
    if ap > 0 and cp > 0 and gp > 0 and tp > 0:
        entropy = - ((ap*(math.log2(ap))) + (cp*(math.log2(cp))) + (gp*(math.log2(gp))) + ap*(math.log2(ap)))
        return entropy
    elif ap == 0 or cp == 0 or gp == 0 or tp == 0:
        return 'Cannot compute due to 0 count'





print(findE(4,2,3,7))       # Entropy = 1.827
print(findE(1,1,1,1))       # Entropy = 2
print(findE(4,4,0,0))       # Entropy = Cannot Compute
# Can do elif ap == 0 and cp > 0 and gp > 0 and tp > 0, but too many lines?? test test
