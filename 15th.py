def calc(*numbers):
	sum = 0
	for n in numbers:
		sum  = sum + n*n
	return sum

print('====calc(*numbers)====')
print(calc(1))
print(calc(1, 2))
print(calc(1, 3, 5))
print(calc(1, 2, 3))
