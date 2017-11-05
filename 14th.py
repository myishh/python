#default parameter

def power(x, n=2):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s

print(power(4))
print(power(4, 1))
print(power(4, 3))

print('--------addend(L=[])--------')
def addend(L=[]):
	L.append('End')
	return L

print(addend())
print(addend())
print(addend())

print('--------addend(L=None)--------')
def addend(L=None):
	if L is None:
		L = []
	L.append('End')
	return L

print(addend())
print(addend())
print(addend())

