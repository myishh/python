def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		print(b)
		a, b = b, a + b
		n = n +1
	return 'done'
print('-------- fib(6)--------')
fib(6)

# This is an generator instead of function
def fib2(max):
	n, a, b = 0, 0, 1
	while n < max:
		#print(b)
		yield b
		a, b = b, a + b
		n = n + 1
	return 'done'
print('-------- fib2(8)--------')
fib2(8) #This is can not be done by using this argument
for n in fib(8):
	print(n)


print('--- fib2(8) using while loop ---')
g = fib2(8)
while True:
	try:
		x = next(g)
		print('g', x)
	except StopIteration as e:
		print('Generator return value:', e.value)
		break


#这里，最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
#举个简单的例子，定义一个generator，依次返回数字1，3，5：

def odd():
	print('step1')
	yield 1
	print('step2')
	yield (3)
	print('step3')
	yield(5)

o = odd()
next(o)
next(o)
next(o)
next(o)
