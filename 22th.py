def f(x):
	return x * x


r = map(f, [1,2,3,4,5,6,7,8,9])
#list(r)
#print(r)
print(list(r))

L = []
for n in [1,2,3,4,5,6,7,8,9]:
	L.append(f(n))
print(L)

print('map()作为高阶函数，事实上它把运算规则抽象了，因此，我们不但可以计算简单的f(x)=x2，还可以计算任意复杂的函数，比如，把这个list所有数字转为字符串：\n')
print('list(map(str, [1,2,3,4,5,6,7,8,9]))')
print(list(map(str, [1,2,3,4,5,6,7,8,9])))


print('**********************************\nreduce把结果继续和序列的下一个元素做累积计算，其效果就是：')
print('reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)\n比方说对一个序列求和，就可以用reduce实现：')

from functools import reduce
def add(x, y):
	return x + y

print('reduce(add, [1,3,5,7]) =', reduce(add, [1,3,5,7]))

from functools import reduce
def fn(x, y):
	return x * 10 + y

print('reduce(fn, [1,3,5,7,9]) =', reduce(fn, [1,3,5,7,9]))

from functools import reduce
def fn(x, y):
	return x * 10 + y
def char2num(s):
	return {'0': 0, '1': 1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7 }[s]

print('reduce(fn, map(char2num, \'13567\')) =',reduce(fn, map(char2num, '13567')))


from functools import reduce
def str2int(s):
	def fn(x, y):
		return x * 10 + y
	def char2num(s):
		return {'0': 0, '1': 1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[s]
	return reduce(fn, map(char2num, s))
print('str2int(\'1989\') =',str2int('1989'))

print('------After Lambda Simplification------')

from functools import reduce
def char2num(s):
	return {'0': 0, '1': 1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[s]

def str2int2(s):
	return reduce(lambda x, y: x * 10 + y, map(char2num, s))

print('str2int2(\'1989\') =',str2int2('1989'))
