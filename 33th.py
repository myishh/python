def printinfo(name, age = 35):
	print('Name = \t', name)
	print('Age =\t', age)

printinfo('Mike')
printinfo('Jack', 66)

def funclen(arg1, *varss):
	print('-'*10+'Demo func len'+ '-'*10)
	print(arg1)
	for var in varss:
		print (var)

funclen(12.88)
funclen('Ma', 'Yun', 'Pony', 'Bill', 77)
