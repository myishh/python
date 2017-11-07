def myabs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x

print(myabs(120))
print(myabs(-99.8))
print(myabs('AA'))
