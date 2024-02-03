import math
import sys

def findF1(tp,fp,tn,fn):
    recall = tp/(tp + fn)
    precision = tp/(tp + fp)

    if tp + tn + fp + fn == 0 or tp + fn == 0 or tp + fp == 0: 
        sys.exit('ERROR: Denominaror Must NOT be 0')

    elif recall + precision == 0 and tp == 0:
        return 'Accuracy is 0, F1 score is 0'

    else: 
        acc = (tp + tn)/(tp + tn + fp +fn)
        f1 = (2 * precision * recall)/(precision + recall)
        return acc,f1

print(findF1(2,3,4,1))  # acc = 0.6, f1 = 0.500
# how to present the result seperately? like accuracy is acc, f1_score is f1

print(findF1(8,4,0,0))  # acc = 0.666, f1=0.800

print(findF1(0,7,0,4))  # accuracy is 0, f1 score is 0

print(findF1(0,7,1,4))  # acc=0.083, f1=0
