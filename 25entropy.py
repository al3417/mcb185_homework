import math

def find_e(a, c, g, t):
    total = a + c + g + t

    if total == 0:  return '0'
    
    if a > 0:   
            p_a = a / total 
            e_a = -(p_a) * (math.log2(p_a))
    else:   e_a = 0

    if c > 0:   
            p_c = c / total 
            e_c = -(p_c) * (math.log2(p_c))
    else:   e_c = 0

    if g > 0:   
            p_g = g / total 
            e_g = -(p_g) * (math.log2(p_g))
    else:   e_g = 0

    if t > 0:   
            p_t = t / total 
            e_t = -(p_t) * (math.log2(p_t))
    else:   e_t = 0
    
    entropy = (e_a + e_c + e_g + e_t)
    
    return entropy
               
   



print(find_e(4,2,3,7))       # Entropy = 1.849
print(find_e(1,1,1,1))       # Entropy = 2
print(find_e(4,4,0,0))       # Entropy = 1.0
print(find_e(2,0,2,0))       # Entropy = 1.0
