import math

def find_tm(a, c, g, t):
    if a + c + g + t <= 13:
        t_m = (a + t) * 2 + (g + c) * 4
        return t_m
    else:
        t_m = 64.9 + 41 * (g + c - 16.4) / (a + t + g + c)
        return t_m

print('The melting temperature of AACCGGTT is :' + str(find_tm(2,2,2,2)))            # 24

print('The melting temperature of AACCCCGGTTTTTTTT is :' + str(find_tm(2,4,2,8)))    # 38.25




