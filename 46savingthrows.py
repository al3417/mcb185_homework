import random

def saving_throw(dc, ad, ds):
	r1 = random.randint(1, 20)
	roll = r1
	r2 = random.randint(1, 20)
	if ad == 1:
		if r1 > r2: roll = r1
		else:		roll = r2
	elif ds == 1:
		if r1 < r2: roll =r1
		else:		roll = r2
	
	return roll >= dc	# boolean result

times = 1000
def calc_prob(dc):
	normal_s = 0
	ad_s = 0
	ds_s = 0
	
	for i in range(times):
# all True result from saving_throw()
		if saving_throw(dc, 0, 0) == True:
			normal_s += 1
		if saving_throw(dc, 1, 0) == True:
			ad_s += 1
		if saving_throw(dc, 0, 1) == True:
			ds_s += 1

	normal_prob = normal_s / times
	ad_prob = ad_s / times
	ds_prob = ds_s / times

	return normal_prob, ad_prob, ds_prob

# dc=5
print(calc_prob(5))
# dc=10
print(calc_prob(10))
# dc=15
print(calc_prob(15))

