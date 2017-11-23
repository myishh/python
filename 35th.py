a = 100

def t1():
	#如果在函数中修改全局变量，那么就需要使用global进行声明，否则出错
	global a
	print('t1 before change, a = %d'%a)
	a = 200
	print('t1 after change, a = %d'%a)

def t2():
	print('a = %d'%a)

t1()
t2()

print()
print('-'*10 + 'Demo Recursion' + '-'*10)
print()

def calNum(num):
	if num > 1:
		result = num * calNum(num - 1)
	else:
		result = 1
	return result

n = 8
print('calNum(%d) = %d'%(n, calNum(n)))
