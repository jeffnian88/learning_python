# pair braces
tel = {'jack': 4098, 'sape': 4139}
print tel

# list of tuple
tel1 = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print tel1

#
tel2 = dict(sape=4139, guido=4127, jack=4098)
print tel2


tel3 = {x: x**2 for x in (2, 4, 6)}
print tel3

tel41=['jack', 'sape']
tel42=[4098,4139]
tel4 = dict(zip(tel41,tel42))
print tel4

# dict initialization
d1 = {}
str1='abcdefg'
for x in str1:
	if x in d1:
		d1[x]=d1[x]+1
	else:
		d1[x]=1
print d1
del d1['a']
print d1
