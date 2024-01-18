import math

def findE(a, c, g, t):
    total = a + c + g + t

    if total == 0:
        return '0'

    def proportion(count):
        if count > 0:
            pos = count / total
            return -(pos) * (math.log2(pos))
        else: return 0

    entropy = (proportion(a) + proportion(c) + proportion(g) + proportion(t))
    
    return entropy


print(findE(4,2,3,7))       # Entropy = 1.849
print(findE(1,1,1,1))       # Entropy = 2
print(findE(4,4,0,0))       # Entropy = 1.0

