#coding=utf-8
import os
L = [d for d in os.listdir('.')]
print(L)

print('\n--------------\n')
d = {'x':'AA','y':'BB', 'z':'CC'}
for k, v in d.items():
	print(k, '=', v)


print('\n--------------\n')

d = {'x':'AA','y':'BB', 'z':'CC'}
L = [k + '=' + v for k, v in d.items()]
print(L)

print('\n---------------\n')
L = ['Hello', 'World', 'IBM', 'Apple']
nl = [s.lower() for s in L]
print(nl)
