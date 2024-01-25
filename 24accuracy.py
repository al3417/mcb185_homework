import math
import sys

def find_af(tp, fp, tn, fn):

    if      tp + tn + fp + fn == 0 or tp + fn == 0 or tp + fn == 0: sys.exit('ERROR: Denominator Must NOT be 0')

    elif    tp + tn == 0:
        return      0,0

    elif    tp == 0 and tn != 0:
        acc         = (tp + tn) / (tp + tn + fp + fn)
        f1          = 0
        return      acc,f1    

    else:    
        acc         = (tp + tn) / (tp + tn + fp + fn)
        recall      = tp / (tp + fn)
        precision   = tp / (tp + fp)
        f1          = (2*precision*recall) / (precision + recall)
        return      acc,f1

print(find_af(2,3,4,1))  # acc = 0.6, f1 = 0.500

print(find_af(8,4,0,0))  # acc = 0.666, f1=0.800

print(find_af(0,7,0,4))  # accuracy is 0, f1 score is 0

print(find_af(0,7,1,4))  # acc=0.083, f1=0

print(find_af(0,0,0,0))  # Denominator Must Not be 0
