import math

def findE(a, c, g, t):
    total = a + c + g + t

    if total == 0:
        return '0'

    def ind_entropy(nt_count):
        if nt_count > 0:
            p = nt_count / total
            return -(p) * (math.log2(p))
        else: return 0

    entropy = (ind_entropy(a) + ind_entropy(c) + ind_entropy(g) + ind_entropy(t))
    
    return entropy


print(findE(4,2,3,7))       # Entropy = 1.849
print(findE(1,1,1,1))       # Entropy = 2
print(findE(4,4,0,0))       # Entropy = 1.0
print(findE(2,0,2,0))       # Entropy = 1.0
