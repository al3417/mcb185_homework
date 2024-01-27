import math
import sys

def find_af(tp, fp, tn, fn):

	if tp + fp != 0 and tp + fn != 0:
		pre =	tp / (tp + fp)
		rec	=	tp / (tp + fn)

		if pre != 0 and rec != 0:
			return (tp + tn) / (tp + tn + fp + fn), ((2 * pre * rec) / (pre + rec))
		elif tp == 0:
			return 	(tp + tn) / (tp + tn + fp + fn), 0
		else:
			return 0,0







print(find_af(2,3,4,1))	# acc = 0.6, f1 = 0.500

print(find_af(8,4,0,0))	# acc = 0.666, f1=0.800

print(find_af(0,7,0,4))	# accuracy is 0, f1 score is 0

print(find_af(0,7,5,4))	# acc=0.3125, f1=0

print(find_af(0,0,0,0))	# NOne
