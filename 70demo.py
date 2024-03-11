# Basic
# dictionary is like a list but with string instead of numeric indices.

list[0] # 0 is numeric index
dict['hey']	#'hey' is a string index
# there is no append() for dict, each item is value pair. 
# The key is the string in square bracket. 
# The value is anything you can put in a variable

d = {}
d = dict()

d = {'dog': 'woof', 'cat': 'meow'}	# to make a dictionary
print(d)	# 'dog' is key for 'woof'


print(d['cat'])	# to access items

d['pig'] = 'oink'	# to add new items to a dict
print(d)

d['cat'] = 'mew'	# to change the value using its key
print(d)

del d['cat']	# to delete an item, use del with its key. del mew
print(d)

# access a key that doesnt exist, get an error
# to check if a key exists, use the keyword 'in'

if 'dog' in d: print(d['dog'])	# key dog, get woof


# Iteration
# use for loop
for key in d: print(f'{key} says {d[key]}')
# or use dict.item()
for k, v in d.items(): print(k, 'says', v)
# unpack tuples
for thing in d.items(): print(thing[0], thing[1])
# if you want just the keys or just the values
print(d.keys(), d.values(), list(d.values())) 
# method dict.keys() and dict.values()

# composition
count = {}
for nt in seq:
	if nt not in count: count[nt] = 0
	count[nt] += 1

# sorting



